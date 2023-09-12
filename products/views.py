from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from django.contrib.auth.models import User
from .models import Product, Category
from reviews.models import Review

# Create your views here.


def all_products(request):
    """
    A view to show all products, including sorting & searching
    """

    # Gets products from DB
    products = Product.objects.all()

    # Resets variables for sort/search
    query = None
    category = None
    sort = None
    direction = None

    if request.GET:

        # Handles product sorting based on sortkey & direction
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

        # Handles product filtering by category
        if 'category' in request.GET:
            category = request.GET['category']
            products = products.filter(category__name=category)
            category = Category.objects.get(name=category)

        # Handles product search
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't search for anything!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(
                description__icontains=query)
            products = products.filter(queries)

    # Sets current sorting & direction
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

    # Gets product from DB
    product = get_object_or_404(Product, pk=product_id)

    # Gets product reviews from DB
    reviews = product.reviews.all().order_by('-rating', '-created_on')

    context = {
        'product': product,
        'reviews': reviews,
    }

    return render(request, 'products/product_detail.html', context)
