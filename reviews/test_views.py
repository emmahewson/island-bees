from django.test import TestCase
from django.urls import reverse
from .models import *
from products.models import Product, Category


class TestReviewsViews(TestCase):
    """ Test product model url views """

    def setUp(self):
        """
        Creates test objects for Reviews app
        """

        userTest = User.objects.create_user(
            username="user1",
            password="password1",
            email='testuseremail@email.com',
        )
        userTest.save()
        
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
            image_url='my image url',
            image='image-file'
        )

        self.reviewTest = Review.objects.create(
            product=self.productTest,
            user=userTest,
            title="test review title",
            content="test review content",
            rating=3,
            created_on="Aug. 10, 2023",

        )

    def test_add_review_page(self):
        """ Test add_review view """

        logged_in = self.client.login(
            username='user1', password='password1')
        self.assertTrue(logged_in)

        userTest = User.objects.get(username='user1')
        response = self.client.get('/reviews/add_review/1')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reviews/add_review.html')
