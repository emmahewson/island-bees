import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings

from django_countries.fields import CountryField

from products.models import Product
from profiles.models import UserProfile


class Order(models.Model):
    """
    Model for Customer Orders
    """

    order_number = models.CharField(
        max_length=32,
        null=False,
        editable=False
    )
    user_profile = models.ForeignKey(
        UserProfile,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='orders'
    )
    full_name = models.CharField(
        max_length=50,
        null=False,
        blank=False
    )
    email = models.EmailField(
        max_length=254,
        null=False,
        blank=False
    )
    phone_number = models.CharField(
        max_length=20,
        null=True,
        blank=True
    )
    street_address1 = models.CharField(
        max_length=80,
        null=False,
        blank=False
    )
    street_address2 = models.CharField(
        max_length=80,
        null=True,
        blank=True
    )
    town_or_city = models.CharField(
        max_length=40,
        null=False,
        blank=False
    )
    county = models.CharField(
        max_length=80,
        null=False,
        blank=False
    )
    postcode = models.CharField(
        max_length=20,
        null=False,
        blank=False
    )
    country = CountryField(
        blank_label='Country *',
        null=False,
        blank=False
    )
    date = models.DateTimeField(
        auto_now_add=True
    )
    order_total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=False, default=0
    )
    delivery_cost = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=False, default=0
    )
    grand_total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=False, default=0
    )
    original_bag = models.TextField(
        null=False,
        blank=False,
        default=''
    )
    stripe_pid = models.CharField(
        max_length=254,
        null=False,
        blank=False,
        default=''
    )

    def _generate_order_number(self):
        """
        Generate a unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update grand total each time a line item is added,
        accounting for delivery costs on items which
        charge for delivery.
        """

        # Calculates the order total without delivery
        self.order_total = float(self.lineitems.aggregate(
            Sum('lineitem_total'))['lineitem_total__sum']) or float(0)

        # Calculate delivery costs based on if product charges for delivery
        total_for_delivery = self.lineitems.filter(
            product__delivery_charge=True).aggregate(
                Sum('lineitem_total'))['lineitem_total__sum']

        # Converts total_for_delivery to a float - avoids calculation errors
        # Checks the total has a value
        if total_for_delivery is not None:
            # Checks the value is above 0 & converts to a float
            if total_for_delivery > 0:
                total_delivery_chargeable = float(total_for_delivery)
            # Converts the value to a float if 0
            else:
                total_delivery_chargeable = float(0)
        # If total_for_delivery has no value sets it to a float of 0
        else:
            total_delivery_chargeable = float(0)

        # Checks if total qualifies for free delivery
        # and calculates delivery charge
        if self.order_total < settings.FREE_DELIVERY_THRESHOLD:
            self.delivery_cost = (
                total_delivery_chargeable * (
                    settings.STANDARD_DELIVERY_PERCENTAGE
                ) / 100)
        else:
            self.delivery_cost = 0.00

        # Calculates total including delivery
        self.grand_total = self.order_total + self.delivery_cost
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    """
    Model for Line Items on a Customer Order
    """

    order = models.ForeignKey(
        Order,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name='lineitems'
    )
    product = models.ForeignKey(
        Product,
        null=False,
        blank=False,
        on_delete=models.PROTECT,
        related_name='lineitems'
    )
    quantity = models.IntegerField(
        null=False,
        blank=False,
        default=0
    )
    lineitem_total = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=False,
        blank=False,
        editable=False
    )

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the order total.
        """
        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.product.name} on order {self.order.order_number}'
