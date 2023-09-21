from django.test import TestCase
from .forms import FaqForm


class TestFaqForm(TestCase):

    def test_faq_question_required(self):
        """ Test the faq question is a required field """
        form = FaqForm({'question': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('question', form.errors.keys())
        self.assertEqual(form.errors['question'][0], 'This field is required.')

    def test_faq_answer_required(self):
        """ Test the faq answer is a required field """
        form = FaqForm({'answer': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('answer', form.errors.keys())
        self.assertEqual(
            form.errors['answer'][0], 'This field is required.')

    def test_fields_are_explicit_in_form_metaclass(self):
        """
        Test that all fields are displayed on form
        """
        form = FaqForm()
        self.assertEqual(form.Meta.fields, '__all__')
        
