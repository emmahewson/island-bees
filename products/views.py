from django.shortcuts import render, get_object_or_404
from .models import Product, Review
from django.db.models import Avg

# Create your views here.


def all_products(request):
    """
    A view to show all products, including sorting & searching
    """

    products = Product.objects.all()

    context = {
        'products': products,
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
