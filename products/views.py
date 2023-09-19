from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, Category
from .forms import ProductForm


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


@login_required
def add_product(request):
    """ Add a new product to the store """

    # Checks user is superuser
    # redirects to home if not
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can add products.')
        return redirect(reverse('home'))

    # Handles Form Submission
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            product = form.save()

            # Gets URL to redirect user back to previous page
            redirect_url = request.POST.get('redirect_url')

            request.session['show_bag_summary'] = False
            messages.success(request, 'Product added successfully.')

            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request, 'Failed to add product. Please check the form.')

    # Handles View Rendering
    else:
        form = ProductForm()

    # Sets page template
    template = 'products/add_product.html'

    # Sets current product & form content
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product """

    # Checks user is superuser
    # redirects to home if not
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can edit products.')
        return redirect(reverse('home'))

    # Get product from DB
    product = get_object_or_404(Product, pk=product_id)

    # Handle Form Submission
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)

        if form.is_valid():
            form.save()

            # Gets URL to redirect user back to previous page
            redirect_url = request.POST.get('redirect_url')

            request.session['show_bag_summary'] = False
            messages.success(request, 'Successfully updated product!')

            return redirect(redirect_url)
        else:
            messages.error(
                request, 'Failed to update product. Please check the form.')

    # Handles View Rendering
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    # Sets page template
    template = 'products/edit_product.html'

    # Sets current product & form content
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product """

    # Gets the previous page URL for redirect
    next = request.GET.get('next', '')

    # Checks user is superuser
    # redirects to home if not
    if not request.user.is_superuser:
        messages.error(
            request, 'Sorry, only store owners can delete products.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()

    request.session['show_bag_summary'] = False
    messages.success(request, 'Product deleted!')
    print(next)

    return redirect(next)
