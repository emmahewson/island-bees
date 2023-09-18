from django.test import TestCase
from products.models import Product, Category


class TestProductsModels(TestCase):
    """
    Test Products App Models
    """

    def setUp(self):
        """
        Creates test objects for Products app
        """

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
        )

    def test_category_string_method(self):
        """ Tests the string method on the category model """
        category = Category(name='Category Name')
        self.assertEqual(str(category), category.name)

    def test_category_string_method_friendly_name(self):
        """ Tests the string method on the category model's friendly name """
        category = Category(friendly_name='Category Friendly Name')
        self.assertEqual(str(category.friendly_name), category.friendly_name)

    def test_product_string_method(self):
        """ Tests the string method on the product model """
        product = Product(name='Product Name')
        self.assertEqual(str(product), product.name)

    def test_product_is_featured_defaults_to_false(self):
        product = Product.objects.create(
            name="A test bee product",
            description="Test description",
            price=3.99
        )
        self.assertFalse(product.is_featured)

    def test_category_name(self):
        """ Test the category name """
        self.assertEqual(self.categoryTest.name, 'Clothing')

    def test_category_friendly_name(self):
        """ Test the category name """
        self.assertEqual(self.categoryTest.friendly_name, 'clothing')

    def test_product_name(self):
        """ Test the product name """
        self.assertEqual(self.productTest.name, 'Bee Suit')

    def test_product_description(self):
        """ Test the product description """
        self.assertEqual(
            self.productTest.description,
            'Test description for Bee Suit'
        )

    def test_product_price(self):
        """ Test the product price """
        self.assertEqual(self.productTest.price, 53.99)

    def test_product_is_featured_field(self):
        """ Test the product is_featured field """
        self.assertTrue(self.productTest.is_featured)
