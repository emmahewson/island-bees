from django.test import TestCase
from django.urls import reverse
from .models import *


class TestProductsViews(TestCase):
    """ Test product model url views """

    def setUp(self):
        """
        Creates test objects for Products app
        """

        self.categoryTest = Category.objects.create(
            name="Clothing",
            friendly_name="clothing",
        )

        self.productTest = Product.objects.create(
            category=self.categoryTest,
            name="Bee Suit",
            description="Test description for Bee Suit",
            price=53.99,
            is_featured=True,
            image_url='my image url'
        )

    def test_products_page(self):
        """ Test products view """
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_product_detail_with_valid_product(self):
        """ Test product detail view works with a valid product """
        response = self.client.get('/products/1/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_detail.html')

    def test_product_detail_page_with_invalid_product(self):
        """ Test product detail view works with an invalid product """
        response = self.client.get('/products/2/')
        self.assertEqual(response.status_code, 404)
