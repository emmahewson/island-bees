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

    def __str__(self):
        """ String representation of Product name """
        return self.name

    """
    MAY WANT TO CHANGE HOW THE RATING WORKS
    MIGHT MAKE MORE SENSE TO ADD A FIELD IN
    THE PRODUCT MODEL WITH THE AVERAGE SCORE
    THIS WOULD NEED TO UPDATE EACH TIME A REVIEW
    IS SAVED - THIS WOULD GO IN THE FORM FUNCTIONALTIY
    This would allow you to order the products by rating
    But perhaps leave the review count @property as it is
    """

    # Adapted from https://github.com/DaveyJH/ci-portfolio-four/
    # blob/main/therapists/models.py#L29-L40
    @property
    def average_rating(self):
        """ Returns average rating of product """
        average = self.reviews.aggregate(Avg('rating'))['rating__avg']

        if average:
            if average.is_integer():
                average = int(average)
            else:
                avg = round(average, 1)

        return average

    @property
    def review_count(self):

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
        ordering = ('-is_featured',)

    def __str__(self):
        """ String representation of Review title """
        return self.title
