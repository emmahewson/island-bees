from django.test import TestCase
from .forms import MessageForm


class TestMessageForm(TestCase):
    """
    Message Form Tests
    """

    def test_message_name_required(self):
        """ Test the message name is a required field """
        form = MessageForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_message_email_required(self):
        """ Test the message email is a required field """
        form = MessageForm({'email': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors.keys())
        self.assertEqual(form.errors['email'][0], 'This field is required.')

    def test_message_subject_required(self):
        """ Test the message subject is a required field """
        form = MessageForm({'subject': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('subject', form.errors.keys())
        self.assertEqual(form.errors['subject'][0], 'This field is required.')

    def test_message_content_required(self):
        """ Test the message content is a required field """
        form = MessageForm({'content': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('content', form.errors.keys())
        self.assertEqual(form.errors['content'][0], 'This field is required.')

    def test_fields_are_explicit_in_form_metaclass(self):
        """
        Test that only the fields
        'name', 'email', 'subject', 'content'
        are displayed on form
        """
        form = MessageForm()
        self.assertEqual(form.Meta.fields, (
            'name', 'email', 'subject', 'content'))
