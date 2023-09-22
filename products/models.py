from django.db import models
from django.core.validators import (
    MaxValueValidator, MinValueValidator
)


class Category(models.Model):

    class Meta:
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        """ String representation of Category name """
        return self.name

    def get_friendly_name(self):
        """ Model Method to return friendly_name """
        return self.friendly_name


class Product(models.Model):

    category = models.ForeignKey(
        'Category',
        null=True,
        blank=True,
        on_delete=models.SET_NULL)

    name = models.CharField(
        max_length=50
    )

    description = models.TextField()

    price = models.DecimalField(
        max_digits=6,
        decimal_places=2
    )

    is_featured = models.BooleanField(
        default=False
    )

    delivery_charge = models.BooleanField(
        default=True
    )

    discontinued = models.BooleanField(
        default=False
    )

    image = models.ImageField(
        null=True,
        blank=True
    )

    rating = models.IntegerField(
        default=0,
        null=True,
        blank=True,
        validators=[
            MaxValueValidator(5, message="Must be between 0-5"),
            MinValueValidator(0, message="Must be between 0-5")
        ],
    )

    def __str__(self):
        """ String representation of Product name """
        return self.name

    @property
    def review_count(self):
        """ Returns total number of reviews """

        return self.reviews.count()
