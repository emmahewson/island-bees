from django.test import TestCase
from django.urls import reverse


class TestProductsViews(TestCase):
    """ Test home url views """

    def test_get_products_page(self):
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')
