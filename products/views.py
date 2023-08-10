from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Avg, Q
from django.db.models.functions import Lower

from django.contrib.auth.models import User
from .models import Product, Review, Category
from .forms import ReviewForm

# Create your views here.


def all_products(request):
    """
    A view to show all products, including sorting & searching
    """

    products = Product.objects.all()
    query = None
    category = None
    sort = None
    direction = None

    if request.GET:

        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == "name":
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower("name"))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == "desc":
                    sortkey = f'-{sortkey}'

            products = products.order_by(sortkey)

        if 'category' in request.GET:
            category = request.GET['category']
            products = products.filter(category__name=category)
            category = Category.objects.get(name=category)

            print(category)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't search for anything!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(
                description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_category': category,
        'current_sorting': current_sorting
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)
    reviews = Review.objects.filter(product=product_id)

    context = {
        'product': product,
        'reviews': reviews,
    }

    return render(request, 'products/product_detail.html', context)


# def add_review(request):
#     """ Add a review """

#     if request.method == 'POST':
#         form = ReviewForm(request.POST, request.FILES)
#         if form.is_valid():
#             review = form.save()
#             messages.success(request, 'Successfully added review!')
#             return redirect(reverse('products'))
#         else:
#             messages.error(
#                 request,
#                 'Failed to add review. Please ensure the form is valid.')
#     else:
#         form = ReviewForm()

#     template = 'products/add_review.html'
#     context = {
#         'form': form,
#     }

#     return render(request, template, context)


def add_review(request, product_id):
    """
    Renders form to add a review
    """

    if request.user:
        author = User.objects.get(username=request.user)
    else:
        author = "Anonymous"

    product = Product.objects.get(id=product_id)
    print(product.id)

    if request.method == "POST":
        form = ReviewForm(request.POST)

        if form.is_valid():
            review = form.save()
            review.product = product
            review.user = author
            review.save()
            messages.success(request, "New product review added.")
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, "Form invalid, please try again.")
    else:
        form = ReviewForm()

    template = 'products/add_review.html'

    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)
