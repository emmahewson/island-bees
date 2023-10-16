from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from checkout.models import OrderLineItem

from .models import Product, Category
from .forms import ProductForm


def all_products(request):
    """
    A view to show all products, including sorting & searching
    """

    # Gets products from DB
    products = Product.objects.filter(discontinued=False)

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
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    # Gets product from DB
    product = get_object_or_404(Product, pk=product_id)

    if product.discontinued:
        messages.info(request, 'That product is no longer available, sorry.')
        return redirect(reverse('products'))

    else:
        # Gets product reviews from DB
        reviews = product.reviews.filter(
            is_approved=True).order_by('-rating', '-created_on')

        # Check if product has ever been ordered
        # protects it from deletion to preserve order history
        lineitems = OrderLineItem.objects.all()
        protected_product = False

        for lineitem in lineitems:
            if product == lineitem.product:
                protected_product = True
                break
            else:
                protected_product = False

        context = {
            'product': product,
            'reviews': reviews,
            'protected_product': protected_product
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

            request.session['show_bag_summary'] = False
            messages.success(request, 'Successfully updated product!')

            # Gets URL to redirect user back to previous page
            redirect_url = request.POST.get('redirect_url')

            # Gets bag from session
            bag = request.session.get('bag', {})

            # Checks 'discontinued' value
            # If item is not discontinued redirects them to previous page
            if request.POST.get('discontinued') is None:
                return redirect(redirect_url)

            # If item is discontinued checks if item is in bag & removes it
            else:
                if str(product.id) in bag:
                    bag.pop(str(product.id))
                    request.session['show_bag_summary'] = True
                    messages.info(
                        request,
                        f'{product.name} discontinued & removed from bag.')

                    # Updates bag in session
                    request.session['bag'] = bag

                # Redirects to 'products'
                return redirect(reverse('products'))
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

    # Checks user is superuser
    # redirects to home if not
    if not request.user.is_superuser:
        messages.error(
            request, 'Sorry, only store owners can delete products.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)

    # Check if product has ever been ordered
    # protects it from deletion to preserve order history
    lineitems = OrderLineItem.objects.all()

    for lineitem in lineitems:
        if product == lineitem.product:
            protected_product = True
            break
        else:
            protected_product = False

    if protected_product:

        # If product is protected set it to discontinued
        product.discontinued = True
        product.save()

        # Checks if item is in bag & removes it
        bag = request.session.get('bag', {})
        if str(product.id) in bag:
            bag.pop(str(product.id))

            # Updates bag in session
            request.session['bag'] = bag

            message = 'Product discontinued and removed from the store & bag.'
            request.session['show_bag_summary'] = True

        else:
            message = 'Product discontinued and removed from the store.'
            request.session['show_bag_summary'] = False

        messages.success(request, message)

        # Redirects to 'products'
        return redirect(reverse('products'))
    else:

        # If product is not protected - delete
        product.delete()
        message = 'Product deleted!'

    messages.success(request, message)
    return redirect(reverse('products'))
