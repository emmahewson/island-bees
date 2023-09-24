from django.test import TestCase

from .models import Order
from products.models import Product, Category


class TestCheckoutViews(TestCase):
    """
    Checkout Views Tests
    """

    def setUp(self):

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
            image='image-file'
        )

        self.order = Order.objects.create(
            order_number='1234567890',
            full_name="Test User",
            email="testemail@email.com",
            phone_number="0123456789",
            street_address1="Test Address 1",
            street_address2="Test Address 2",
            town_or_city="Test City",
            county="Test County",
            country="GB",
        )

    def test_get_checkout_page_with_empty_bag(self):
        """ test checkout page redirects to products with empty bag """

        response = self.client.get('/checkout/')
        self.assertTrue(response, '/products')

    def test_get_checkout_page_with_bag_items(self):
        """ test checkout page view with bag items """

        session = self.client.session
        session['bag'] = {str(self.productTest.id): 1}
        session.save()

        response = self.client.get('/checkout/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/checkout.html')
