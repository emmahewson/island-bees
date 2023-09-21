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
            discontinued=True,
            delivery_charge=False,
        )

        self.productTest2 = Product.objects.create(
            category=self.categoryTest,
            name="Hive Tool",
            description="Test description for Hive Tool",
            price=10,
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

    def test_product_discontinued_field(self):
        """ Test the product discontinued field """
        self.assertTrue(self.productTest.discontinued)

    def test_product_delivery_charge_field(self):
        """ Test the product delivery charge field """
        self.assertFalse(self.productTest.delivery_charge)

    def test_product_is_featured_defaults_to_false(self):
        """ Test the is_featured field defaults to False """
        self.assertFalse(self.productTest2.is_featured)

    def test_product_discontinued_defaults_to_false(self):
        """ Test the discontinued field defaults to False """
        self.assertFalse(self.productTest2.discontinued)

    def test_product_delivery_charge_defaults_to_true(self):
        """ Test the delivery charge field defaults to True """
        self.assertTrue(self.productTest2.delivery_charge)
