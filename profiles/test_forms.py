from django.test import TestCase
from .forms import UserForm, UserProfileForm


class TestUserProfileForm(TestCase):
    """
    Profile Form Tests
    """

    def test_not_required_fields(self):
        """ Test User Profile form is valid with empty non-required fields """
        form = UserProfileForm(
            {
                'default_street_address1': '',
                'default_street_address2': '',
                'default_town_or_city': '',
                'default_county': '',
                'default_postcode': '',
                'default_country': '',
                'default_phone_number': '',
            }
            )
        self.assertTrue(form.is_valid())

    def test_user_in_excludes_in_form_metaclass(self):
        """
        Test that 'user' field is excluded from the form's Meta
        """
        form = UserProfileForm()
        self.assertEqual(form.Meta.exclude, ('user',))


class TestUserForm(TestCase):
    """ Testing the User Form """

    def test_not_required_fields(self):
        """ Test User form is valid with empty non-required fields """
        form = UserForm(
            {
                'first_name': '',
                'last_name': '',
            }
            )
        self.assertTrue(form.is_valid())

    def test_fields_are_explicit_in_form_metaclass(self):
        """
        Test that relevant fields are explicit in form's Meta
        """
        form = UserForm()
        self.assertEqual(form.Meta.fields, ('first_name', 'last_name'))
