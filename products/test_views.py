from django.test import TestCase
from django.contrib.auth.models import User

from .models import Product, Category
from checkout.models import Order, OrderLineItem


class TestProductsViews(TestCase):
    """
    Products Views Tests
    """

    def setUp(self):
        """
        Creates test objects for Products app
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
            discontinued=False
        )

        self.productTest2 = Product.objects.create(
            category=self.categoryTest,
            name="Hive Tool",
            description="Test description for Hive Tool",
            price=4,
            is_featured=True,
            discontinued=False
        )

        self.productTest3 = Product.objects.create(
            category=self.categoryTest,
            name="Old Product",
            description="Test description for Old Product",
            price=4,
            is_featured=True,
            discontinued=True
        )

        self.orderTest = Order.objects.create(
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

        self.orderLineItemTest1 = OrderLineItem.objects.create(
            order=self.orderTest,
            product=self.productTest2,
            quantity=1,
        )

    def test_products_page(self):
        """ Test products view """
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_product_detail_with_valid_product(self):
        """ Test product detail view works with a valid product """
        response = self.client.get('/products/1/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_detail.html')

    def test_product_detail_page_with_invalid_product(self):
        """ Test product detail view works with an invalid product """
        response = self.client.get('/products/99/')
        self.assertEqual(response.status_code, 404)

    def test_product_detail_page_with_discontinued_product(self):
        """ Test product detail view works with a discontinued product """
        response = self.client.get('/products/3/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/products/')

    def test_add_product_page_for_logged_out_user(self):
        """ Test add product view for logged out user """

        response = self.client.get('/products/add/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login/?next=/products/add/')

    def test_add_product_page_for_unauthorised_user(self):
        """ Test add product view for logged in user (not superuser) """

        logged_in = self.client.login(
            username='user1', password='password1')
        self.assertTrue(logged_in)

        response = self.client.get('/products/add/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')

    def test_add_product_page_for_superuser(self):
        """ Test add product view for authorised user (superuser) """

        logged_in = self.client.login(
            username='superuser1', password='super_password1')
        self.assertTrue(logged_in)

        response = self.client.get('/products/add/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/add_product.html')

    def test_edit_product_page_for_logged_out_user(self):
        """ Test edit product view for logged out user """

        response = self.client.get('/products/edit/1/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response, '/accounts/login/?next=/products/edit/1/')

    def test_edit_product_page_for_unauthorised_user(self):
        """ Test edit product view for logged in user (not superuser) """

        logged_in = self.client.login(
            username='user1', password='password1')
        self.assertTrue(logged_in)

        response = self.client.get('/products/edit/1/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')

    def test_edit_valid_product_page_for_superuser(self):
        """
        Test edit product view for authorised user (superuser)
        With a valid product id
        """

        logged_in = self.client.login(
            username='superuser1', password='super_password1')
        self.assertTrue(logged_in)

        response = self.client.get('/products/edit/1/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/edit_product.html')

    def test_edit_invalid_product_page_for_superuser(self):
        """
        Test edit product view for authorised user (superuser)
        With an invalid product id
        """

        logged_in = self.client.login(
            username='superuser1', password='super_password1')
        self.assertTrue(logged_in)

        response = self.client.get('/products/edit/99/')
        self.assertEqual(response.status_code, 404)

    def test_delete_product_view_for_logged_out_user(self):
        """
        Checks delete product view for logged out user
        """

        response = self.client.get('/products/delete/1/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response, '/accounts/login/?next=/products/delete/1/')

    def test_delete_product_page_for_unauthorised_user(self):
        """ Test delete product view for logged in user (not superuser) """

        logged_in = self.client.login(
            username='user1', password='password1')
        self.assertTrue(logged_in)

        response = self.client.get('/products/delete/1/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')

    def test_delete_valid_product_page_for_superuser(self):
        """
        Test delete product view for authorised user (superuser)
        With a valid product id
        """

        logged_in = self.client.login(
            username='superuser1', password='super_password1')
        self.assertTrue(logged_in)

        response = self.client.get('/products/delete/1/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/products/')

    def test_delete_invalid_product_page_for_superuser(self):
        """
        Test delete product view for authorised user (superuser)
        With an invalid product id
        """

        logged_in = self.client.login(
            username='superuser1', password='super_password1')
        self.assertTrue(logged_in)

        response = self.client.get('/products/delete/99/')
        self.assertEqual(response.status_code, 404)

    def test_delete_protected_product_page_for_superuser(self):
        """
        Test delete product view for authorised user (superuser)
        With a protected product (appears in a lineitem)
        """

        logged_in = self.client.login(
            username='superuser1', password='super_password1')
        self.assertTrue(logged_in)

        response = self.client.get('/products/delete/2/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/products/')
