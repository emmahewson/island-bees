from django.shortcuts import render
from products.models import Product

# Create your views here.


def index(request):
    """
    A view to return the home page
    """

    # Gets products from DB for featured products section
    products = Product.objects.all()
    context = {
        'products': products,
    }

    return render(request, 'home/index.html', context)
