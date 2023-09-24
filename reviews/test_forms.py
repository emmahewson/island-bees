from django.test import TestCase
from .forms import ReviewForm

# Create your tests here.


class TestReviewForm(TestCase):

    def test_review_title_required(self):
        """ Test the review title is a required field """
        form = ReviewForm({'title': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(form.errors['title'][0], 'This field is required.')

    def test_review_content_required(self):
        """ Test the review content is a required field """
        form = ReviewForm({'content': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('content', form.errors.keys())
        self.assertEqual(form.errors['content'][0], 'This field is required.')

    def test_review_rating_required(self):
        """ Test the review rating is a required field """
        form = ReviewForm({'rating': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('rating', form.errors.keys())
        self.assertEqual(form.errors['rating'][0], 'This field is required.')

    def test_review_rating_min_value(self):
        """ Test the review rating is >= 0 """
        form = ReviewForm({'rating': '-2'})
        self.assertFalse(form.is_valid())
        self.assertIn('rating', form.errors.keys())
        self.assertEqual(form.errors['rating'][0], 'Must be between 0-5')

    def test_review_rating_max_value(self):
        """ Test the review rating is <= 5 """
        form = ReviewForm({'rating': '6'})
        self.assertFalse(form.is_valid())
        self.assertIn('rating', form.errors.keys())
        self.assertEqual(form.errors['rating'][0], 'Must be between 0-5')

    def test_fields_are_explicit_in_form_metaclass(self):
        """
        Test that only the fields
        'title', 'content' & 'rating'
        are displayed on form
        """
        form = ReviewForm()
        self.assertEqual(form.Meta.fields, ('title', 'content', 'rating'))
