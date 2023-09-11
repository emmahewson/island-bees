from django.shortcuts import (
    render, redirect, reverse, get_object_or_404, HttpResponse)
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from .models import Order, OrderLineItem

from products.models import Product
from bag.contexts import bag_contents

import stripe
import json


@require_POST
def cache_checkout_data(request):
    """
    Passes information to the payment intent webhook
    before the confirm card payment method is called in JS
    Includes whether user wants to save their data,
    username and bag contents
    """
    # Saves additional metadata to the payment intent
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'bag': json.dumps(request.session.get('bag', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)

    # Handles errors
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


def checkout(request):
    """
    Handles the checkout functionality including Stripe payments
    and creates a new order in the DB
    """

    # Sets Stripe Keys
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    # Handles Form Submission
    if request.method == 'POST':

        # Gets bag from session
        bag = request.session.get('bag', {})

        # Stores the form data
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }
        order_form = OrderForm(form_data)

        # Handles a valid form submission
        if order_form.is_valid():
            order = order_form.save()

            # Iterates through bag items to create line_items
            for item_id, item_data in bag.items():

                # Checks each product exists in DB
                # If so saves in as an order_line_item
                try:
                    product = Product.objects.get(id=item_id)
                    order_line_item = OrderLineItem(
                        order=order,
                        product=product,
                        quantity=item_data,
                    )
                    order_line_item.save()

                # If product doesn't exist returns an error & deletes order
                except Product.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your bag wasn't "
                        "found in our database. "
                        "Please call us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('view_bag'))

            # Stores whether user wanted to save their form data to profile
            request.session['save_info'] = 'save-info' in request.POST

            # Takes user to Checkout Success page
            return redirect(reverse(
                'checkout_success', args=[order.order_number]))

        # Handles an invalid form submission
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')

    # Handles GET method functionality
    else:
        bag = request.session.get('bag', {})

        # Stops users navigating to checkout with no items in bag
        if not bag:
            messages.error(
                request, "There's nothing in your bag at the moment")
            return redirect(reverse('products'))

        # Gets current bag contents from session
        current_bag = bag_contents(request)

        # Handles Stripe payment amounts for payment intent
        total = current_bag['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        # Populates order form inputs
        order_form = OrderForm()

    # Handles no Stripe Public Key variable
    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    """
    Handle successful checkouts
    Allows users to save data to their profile
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)

    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')

    # Deletes bag from session
    if 'bag' in request.session:
        del request.session['bag']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
