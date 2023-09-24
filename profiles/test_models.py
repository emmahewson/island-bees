from django.test import TestCase
from django.contrib.auth.models import User

from .models import UserProfile


class TestProfileModels(TestCase):
    """
    Profiles Models Tests
    """

    def setUp(self):

        self.user = User.objects.create_user(
            username='test_name',
            first_name='Test',
            last_name='User',
            password='test_password',
            email='testemail@email.com'
        )

        self.user.userprofile.default_street_address1 = "Test Street 1"
        self.user.userprofile.default_street_address2 = "Test Street 2"
        self.user.userprofile.default_town_or_city = "Test Town"
        self.user.userprofile.default_county = "Test County"
        self.user.userprofile.default_postcode = "AA11 1AA"
        self.user.userprofile.default_country = "GB"
        self.user.userprofile.default_phone_number = "1234567890"

        self.user.userprofile.save()

    def test_profile_string_method(self):
        """ Tests the string method on the userProfile model """
        profile = UserProfile(user=self.user)
        self.assertEqual(str(profile), profile.user.username)

    def test_profile_info(self):
        """ Test the order address """
        profile = UserProfile.objects.get(user=self.user)
        self.assertEqual(profile.default_street_address1, 'Test Street 1')
        self.assertEqual(profile.default_street_address2, 'Test Street 2')
        self.assertEqual(profile.default_town_or_city, 'Test Town')
        self.assertEqual(profile.default_county, 'Test County')
        self.assertEqual(profile.default_postcode, 'AA11 1AA')
        self.assertEqual(profile.default_country, 'GB')
        self.assertEqual(profile.default_phone_number, '1234567890')
