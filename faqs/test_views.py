from django.test import TestCase
from django.contrib.auth.models import User

from .models import Faq


class TestFaqsViews(TestCase):
    """ Test FAQs model url views """

    def setUp(self):
        """
        Creates test objects for FAQs app
        """

        userTest = User.objects.create_user(
            username="user1",
            password="password1",
            email='testuseremail@email.com',
        )
        userTest.save()

        superuserTest = User.objects.create_superuser(
            username="superuser1",
            password="super_password1",
            email='testsuperuseremail@email.com',
        )
        superuserTest.save()

        self.faqTest = Faq.objects.create(
            question="Test Question",
            answer="Test Answer",
        )

    def test_faqs_page(self):
        """ Test FAQs view """
        response = self.client.get('/faqs/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'faqs/faqs.html')

    def test_add_faq_page_for_logged_out_user(self):
        """ Test add faq view for logged out user """

        response = self.client.get('/faqs/add/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login/?next=/faqs/add/')

    def test_add_faqs_page_for_unauthorised_user(self):
        """ Test add faqs view for logged in user (not superuser) """

        logged_in = self.client.login(
            username='user1', password='password1')
        self.assertTrue(logged_in)

        response = self.client.get('/faqs/add/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/faqs/')

    def test_add_faq_page_for_superuser(self):
        """ Test add faq view for authorised user (superuser) """

        logged_in = self.client.login(
            username='superuser1', password='super_password1')
        self.assertTrue(logged_in)

        response = self.client.get('/faqs/add/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'faqs/add_faq.html')

    def test_edit_faq_page_for_logged_out_user(self):
        """ Test edit faq view for logged out user """

        response = self.client.get('/faqs/edit/1/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response, '/accounts/login/?next=/faqs/edit/1/')

    def test_edit_faq_page_for_unauthorised_user(self):
        """ Test edit faq view for logged in user (not superuser) """

        logged_in = self.client.login(
            username='user1', password='password1')
        self.assertTrue(logged_in)

        response = self.client.get('/faqs/edit/1/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/faqs/')

    def test_edit_valid_faq_page_for_superuser(self):
        """
        Test edit faq view for authorised user (superuser)
        With a valid faq id
        """

        logged_in = self.client.login(
            username='superuser1', password='super_password1')
        self.assertTrue(logged_in)

        response = self.client.get('/faqs/edit/1/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'faqs/edit_faq.html')

    def test_edit_invalid_faq_page_for_superuser(self):
        """
        Test edit faq view for authorised user (superuser)
        With an invalid faq id
        """

        logged_in = self.client.login(
            username='superuser1', password='super_password1')
        self.assertTrue(logged_in)

        response = self.client.get('/faqs/edit/99/')
        self.assertEqual(response.status_code, 404)

    def test_delete_faq_view_for_logged_out_user(self):
        """
        Checks delete faq view for logged out user
        """

        response = self.client.get('/faqs/delete/1/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response, '/accounts/login/?next=/faqs/delete/1/')

    def test_delete_faq_page_for_unauthorised_user(self):
        """ Test delete faq view for logged in user (not superuser) """

        logged_in = self.client.login(
            username='user1', password='password1')
        self.assertTrue(logged_in)

        response = self.client.get('/faqs/delete/1/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/faqs/')

    def test_delete_valid_faq_page_for_superuser(self):
        """
        Test delete faq view for authorised user (superuser)
        With a valid faq id
        """

        logged_in = self.client.login(
            username='superuser1', password='super_password1')
        self.assertTrue(logged_in)

        response = self.client.get('/faqs/delete/1/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/faqs/')

    def test_delete_invalid_faq_page_for_superuser(self):
        """
        Test delete faq view for authorised user (superuser)
        With an invalid faq id
        """

        logged_in = self.client.login(
            username='superuser1', password='super_password1')
        self.assertTrue(logged_in)

        response = self.client.get('/faqs/delete/99/')
        self.assertEqual(response.status_code, 404)
