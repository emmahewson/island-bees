from django.shortcuts import (
    render, redirect, reverse, get_object_or_404, HttpResponse)
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm


def checkout(request):
    """ Handles the checkout functionality """
    bag = request.session.get('bag', {})

    # Stops users accessing the checkout if there's nothing in their bag
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': (
            "pk_test_51NLQkEJFGU0jclH5qw07G55y0366FNUcgDDXjHZGLmpxfBrBrMm"
            "7uNeKmKAPUq2zKfjX61i2oZTbxNnIYmcIQbZM00xlFBf5MI"),
        'client_secret': 'test client secret key'
    }

    return render(request, template, context)