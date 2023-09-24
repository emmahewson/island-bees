from django.test import TestCase
from datetime import date
from django.utils import timezone
from freezegun import freeze_time

from django.contrib.auth.models import User
from .models import Message


@freeze_time("2022-08-15")
class TestMessageModels(TestCase):
    """
    Test Messages App Models
    """

    def setUp(self):
        """
        Creates test objects for Manage app
        """

        userTest = User.objects.create_user(
            username="user1",
            password="password1",
            email='testuseremail@email.com',
            first_name='F-name',
            last_name='L-name',

        )
        userTest.save()

        self.TestMessage = Message.objects.create(
            user=userTest,
            name=userTest.get_full_name(),
            email=userTest.email,
            subject="Test Subject",
            content="Test Content",
            created_on=timezone.now(),
        )

        self.TestMessage2 = Message.objects.create(
            name="Test Name",
            email="test@test.com",
            subject="Test Subject",
            content="Test Content",
            created_on=timezone.now(),
            is_open=False,
        )

    def test_message_string_method(self):
        """ Tests the string method on the message model """
        message = Message(subject='Test Subject')
        self.assertEqual(str(message), message.subject)

    def test_message_subject(self):
        """ Test the message subject """
        self.assertEqual(self.TestMessage.subject, 'Test Subject')

    def test_message_subject(self):
        """ Test the message content """
        self.assertEqual(self.TestMessage.content, 'Test Content')

    def test_message_created_on(self):
        """ Test the message content """
        self.assertEqual(self.TestMessage.created_on, date(2022, 8, 15))

    def test_message_is_open_field(self):
        """ Test the is_open field """
        self.assertFalse(self.TestMessage2.is_open)

    def test_message_is_open_defaults_to_true(self):
        """ Test the is_open field defaults to True """
        self.assertTrue(self.TestMessage.is_open)

    def test_message_name_for_logged_out_user(self):
        """ Test the message name for a logged out user """
        self.assertEqual(self.TestMessage2.name, 'Test Name')

    def test_message_email_for_logged_out_user(self):
        """ Test the message email for a logged out user """
        self.assertEqual(self.TestMessage2.email, 'test@test.com')

    def test_message_name_for_logged_in_user(self):
        """ Test the message name for a logged in user """
        self.assertEqual(self.TestMessage.name, 'F-name L-name')

    def test_message_email_for_logged_in_user(self):
        """ Test the message email for a logged in user """
        self.assertEqual(self.TestMessage.email, 'testuseremail@email.com')
