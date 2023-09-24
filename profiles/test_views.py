from django.test import TestCase
from django.contrib.auth.models import User
from .models import UserProfile
from checkout.models import Order


class TestProfileViews(TestCase):
    """
    Profile Views Tests
    """

    def setUp(self):

        testUser = User.objects.create_user(
            username='test_name',
            first_name='Test',
            last_name='User',
            password='test_password',
            email='testemail@email.com'
        )
        testUser.save()

        Order.objects.create(
            order_number='1234567890',
            user_profile=UserProfile.objects.get(user=testUser),
            full_name="Test User",
            email="testemail@email.com",
            phone_number="0123456789",
            street_address1="Test Address 1",
            street_address2="Test Address 2",
            town_or_city="Test City",
            county="Test County",
            country="GB",
        )

    def test_profile_page_url_get(self):
        """ Test user profile page view and template """

        self.client.login(username='test_name', password="test_password")
        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')

    def test_order_history_view(self):
        """ Test order detail view & template """
        self.client.login(username='test_name', password="test_password")
        testuser = User.objects.get(username='test_name')
        order = Order.objects.get(email=testuser.email)
        response = self.client.get(
            '/profile/order_history/' + order.order_number)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/checkout_success.html')
