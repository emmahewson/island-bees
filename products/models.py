from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg
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
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(
        max_length=254)
    description = models.TextField()
    price = models.DecimalField(
        max_digits=6, decimal_places=2)
    is_featured = models.BooleanField(default=False, blank=True)
    image_url = models.URLField(
        max_length=1024, null=True, blank=True)
    image = models.ImageField(
        null=True, blank=True)
    rating = models.IntegerField(
        default=0, null=True, blank=True,
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


class Review(models.Model):
    """ Review Model """
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        null=True, blank=True,
        related_name="reviews",
    )
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True
    )
    created_on = models.DateField(auto_now_add=True, blank=False, null=False)
    title = models.CharField(max_length=40)
    content = models.TextField(max_length=500)
    is_featured = models.BooleanField(default=False, blank=True)
    rating = models.IntegerField(
        validators=[
            MaxValueValidator(5, message="Must be between 0-5"),
            MinValueValidator(0, message="Must be between 0-5")
        ],
        default=0, blank=False, null=False
    )

    class Meta:
        ordering = ('-is_featured', 'created_on')

    def __str__(self):
        """ String representation of Review title """
        return self.title
