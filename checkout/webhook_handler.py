from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from .models import Order, OrderLineItem
from products.models import Product
from profiles.models import UserProfile

import stripe
import json
import time


class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    # Private method to send user information email when placing order
    def _send_confirmation_email(self, order):
        """Send the user a confirmation email"""
        cust_email = order.email
        subject = render_to_string(
            'checkout/confirmation_emails/confirmation_email_subject.txt',
            {'order': order})
        body = render_to_string(
            'checkout/confirmation_emails/confirmation_email_body.txt',
            {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL})

        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [cust_email]
        )

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

        # Update profile information if save_info was checked
        # Allows anonymous users to still checkout
        profile = None
        username = intent.metadata.username

        # Checks if user is logged in
        if username != 'AnonymousUser':
            profile = UserProfile.objects.get(user__username=username)
            # Checks if user wants to save info
            if save_info == "true":
                profile.default_phone_number = shipping_details.phone
                profile.default_country = shipping_details.address.country
                profile.default_postcode = shipping_details.address.postal_code
                profile.default_town_or_city = shipping_details.address.city
                profile.default_street_address1 = (
                    shipping_details.address.line1)
                profile.default_street_address2 = (
                    shipping_details.address.line2)
                profile.default_county = shipping_details.address.state
                profile.save()

        # Check if order exists and if not create it
        # Avoids errors if user closes browser
        # or process is interrupted
        order_exists = False
        attempt = 1

        # Makes 5 attempts to find order in DB
        # Avoids duplicating orders if view is slow to create Order
        while attempt <= 5:
            print(f'Attempt {attempt}: Order Exists: {order_exists}')
            try:
                order = Order.objects.get(
                    full_name__iexact=shipping_details.name,
                    email__iexact=billing_details.email,
                    country__iexact=shipping_details.address.country,
                    postcode__iexact=shipping_details.address.postal_code,
                    town_or_city__iexact=shipping_details.address.city,
                    street_address1__iexact=shipping_details.address.line1,
                    county__iexact=shipping_details.address.state,
                    grand_total=grand_total,
                    original_bag=bag,
                    stripe_pid=pid,
                )

                # Sets value to True if order is found
                order_exists = True
                print(f'Found order! Order Exists: {order_exists}')
                break
            # Reattempts to find order if fails (5 times over 5 seconds)
            except Order.DoesNotExist:
                print("Trying again...")
                attempt += 1
                time.sleep(1)

        # If order is found in DB returns message & sends confirmation email
        if order_exists:
            self._send_confirmation_email(order)
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | ' +
                'SUCCESS: Verified order already in database',
                status=200)

        # If order is not found in DB create order
        else:
            print("Order not found - Webhook Creating an order")
            order = None
            # Attempts to create order
            try:
                order = Order.objects.create(
                    full_name=shipping_details.name,
                    user_profile=profile,
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

        # Send confirmation email
        self._send_confirmation_email(order)

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
