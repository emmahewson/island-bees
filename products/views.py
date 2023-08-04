from django.shortcuts import render
from .models import Product

# Create your views here.


def all_products(request):
    """
    A view to show all products, including sorting & searching
    """

    products = Product.objects.all()

    context = {
        'products': products,
        'rating': 5,  # Need to create code for this
    }

    return render(request, 'products/products.html', context)
