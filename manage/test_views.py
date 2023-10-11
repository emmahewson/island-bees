from django.test import TestCase
from django.utils import timezone
from django.contrib.auth.models import User

from .models import Message


class TestManageViews(TestCase):
    """
    Manage Views Tests
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

        superuserTest = User.objects.create_superuser(
            username="superuser1",
            password="super_password1",
            email='testsuperuseremail@email.com',
        )
        superuserTest.save()

        self.TestMessage = Message.objects.create(
            id=1,
            user=userTest,
            name=userTest.get_full_name(),
            email=userTest.email,
            subject="Test Subject",
            content="Test Content",
            created_on=timezone.now(),
            is_open=True,
        )

    def test_contact_us_page(self):
        """ Test Contact Us Page view """
        response = self.client.get('/manage/contact_us')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'manage/contact_us.html')

    def test_manage_page_for_authorized_user(self):
        """ Test manage site view for superuser """

        logged_in = self.client.login(
            username='superuser1', password='super_password1')
        self.assertTrue(logged_in)

        response = self.client.get('/manage/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'manage/manage.html')

    def test_manage_page_for_unauthorized_user(self):
        """ Test manage site view for non superuser """

        logged_in = self.client.login(
            username='user1', password='password1')
        self.assertTrue(logged_in)

        response = self.client.get('/manage/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response, '/')

    def test_manage_page_for_logged_out_user(self):
        """
        Checks manage page redirects to login
        if user is not logged in
        """

        response = self.client.get('/manage/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response, '/accounts/login/?next=/manage/')

    def test_toggle_message_for_logged_out_user(self):
        """ Test toggle message view for logged out """

        response = self.client.get('/manage/toggle/1/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response, '/accounts/login/?next=/manage/toggle/1/')
