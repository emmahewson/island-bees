from django.http import HttpResponse

from .models import Order, OrderLineItem
from products.models import Product

import stripe
import json
import time


class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        # Get payment intent
        intent = event.data.object

        # Get ID of payment intent
        pid = intent.id

        # Get bag from payment intent
        bag = intent.metadata.bag

        # Get value of 'save_info' box from payment intent
        save_info = intent.metadata.save_info

        # Retrieve information from payment intent

        # Get the charge object
        stripe_charge = stripe.Charge.retrieve(
            intent.latest_charge
        )
        # Get the billing and shipping details
        billing_details = stripe_charge.billing_details
        shipping_details = intent.shipping

        # Get the total charge
        grand_total = round(stripe_charge.amount / 100, 2)

        # Set empty values in shipping details to None
        # rather than blank strings
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        # Check if order exists and if not create it
        # Avoids errors if user closes browser
        # or process is interrupted
        order_exists = False
        attempt = 1

        # Makes 5 attempts to find order in DB
        # Avoids duplicating orders if view is slow to create Order
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    full_name__iexact=shipping_details.name,
                    email__iexact=billing_details.email,
                    phone_number__iexact=shipping_details.phone,
                    country__iexact=shipping_details.address.country,
                    postcode__iexact=shipping_details.address.postal_code,
                    town_or_city__iexact=shipping_details.address.city,
                    street_address1__iexact=shipping_details.address.line1,
                    street_address2__iexact=shipping_details.address.line2,
                    county__iexact=shipping_details.address.state,
                    grand_total=grand_total,
                    original_bag=bag,
                    stripe_pid=pid,
                )

                # Sets value to True if order is found
                order_exists = True
                break
            # Reattempts to find order if fails (5 times over 5 seconds)
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)

        # If order is found in DB returns message & sends confirmation email
        if order_exists:
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | ' +
                'SUCCESS: Verified order already in database',
                status=200)

        # If order is not found in DB create order
        else:
            order = None
            # Attempts to create order
            try:
                order = Order.objects.create(
                    full_name=shipping_details.name,
                    email=billing_details.email,
                    phone_number=shipping_details.phone,
                    country=shipping_details.address.country,
                    postcode=shipping_details.address.postal_code,
                    town_or_city=shipping_details.address.city,
                    street_address1=shipping_details.address.line1,
                    street_address2=shipping_details.address.line2,
                    county=shipping_details.address.state,
                    original_bag=bag,
                    stripe_pid=pid,
                )
                # Iterates through bag items to create order_line_items
                for item_id, item_data in json.loads(bag).items():
                    product = Product.objects.get(id=item_id)
                    order_line_item = OrderLineItem(
                        order=order,
                        product=product,
                        quantity=item_data,
                    )
                    order_line_item.save()

            # Handles errors during attempt to create order
            # Deletes the order & returns error message
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)

        return HttpResponse(
            content=f'Webhook received: {event["type"]} | ' +
            'SUCCESS: Created order in webhook',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
