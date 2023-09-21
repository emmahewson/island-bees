from django.test import TestCase

from .models import Faq


class TestFaqsModels(TestCase):
    """
    Test FAQS App Models
    """

    def setUp(self):
        """
        Creates test objects for FAQs app
        """

        self.faqTest = Faq.objects.create(
            question="Test Question",
            answer="Test Answer",
        )

    def test_faq_string_method(self):
        """ Tests the string method on the faq model """
        faq = Faq(question="Test Question")
        self.assertEqual(str(faq), faq.question)

    def test_faq_question(self):
        """ Test the faq question """
        self.assertEqual(self.faqTest.question, "Test Question")

    def test_faq_answer(self):
        """ Test the faq answer """
        self.assertEqual(self.faqTest.answer, "Test Answer")
