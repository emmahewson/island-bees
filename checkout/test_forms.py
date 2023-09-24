from django.test import TestCase
from .forms import OrderForm


class TestOrderForm(TestCase):
    """
    Order Form Tests
    """

    def test_name_required(self):
        """ Test the full name is a required field """
        form = OrderForm({'full_name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('full_name', form.errors.keys())
        self.assertEqual(
            form.errors['full_name'][0], 'This field is required.')

    def test_email_required(self):
        """ Test the email is a required field """
        form = OrderForm({'email': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors.keys())
        self.assertEqual(form.errors['email'][0], 'This field is required.')

    def test_street1_required(self):
        """ Test street address 1 is a required field """
        form = OrderForm({'street_address1': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('street_address1', form.errors.keys())
        self.assertEqual(
            form.errors['street_address1'][0], 'This field is required.')

    def test_town_required(self):
        """ Test town or city is a required field """
        form = OrderForm({'town_or_city': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('town_or_city', form.errors.keys())
        self.assertEqual(
            form.errors['town_or_city'][0], 'This field is required.')

    def test_county_required(self):
        """ Test county is a required field """
        form = OrderForm({'county': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('county', form.errors.keys())
        self.assertEqual(
            form.errors['county'][0], 'This field is required.')

    def test_postcode_required(self):
        """ Test postcode is a required field """
        form = OrderForm({'postcode': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('postcode', form.errors.keys())
        self.assertEqual(
            form.errors['postcode'][0], 'This field is required.')

    def test_country_required(self):
        """ Test country is a required field """
        form = OrderForm({'country': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('country', form.errors.keys())
        self.assertEqual(
            form.errors['country'][0], 'This field is required.')

    def test_not_required_fields(self):
        """ Test form is valid with empty non-required fields """
        form = OrderForm(
            {
                'full_name': 'Test',
                'email': 'test@test.com',
                'phone_number': '',
                'street_address1': 'Test',
                'street_address2': '',
                'town_or_city': 'Test',
                'county': 'Test',
                'postcode': 'Test',
                'country': 'GB',
            }
            )
        self.assertTrue(form.is_valid())

    def test_fields_are_explicit_in_form_metaclass(self):
        """
        Test that only the fields
        'full_name', 'email', 'phone_number',
        'street_address1', 'street_address2',
        'town_or_city', 'postcode', 'country',
        'county'
        are displayed on form
        """
        form = OrderForm()
        self.assertEqual(form.Meta.fields, (
            'full_name', 'email', 'phone_number',
            'street_address1', 'street_address2',
            'town_or_city', 'postcode', 'country',
            'county')
        )
