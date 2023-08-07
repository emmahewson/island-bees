from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.


def all_products(request):
    """
    A view to show all products, including sorting & searching
    """

    products = Product.objects.all()

    context = {
        'products': products,
        'rating': 0,  # Need to create code for this
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
        'rating': 3,  # Need to create code for this
    }

    return render(request, 'products/product_detail.html', context)
