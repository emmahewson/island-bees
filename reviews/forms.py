from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    """
    Add / Edit Review form
    """

    class Meta:
        model = Review
        fields = ('title', 'content', 'rating',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'title': 'Title',
            'content': 'You Review',
            'rating': 0
        }

        self.fields['title'].widget.attrs['autofocus'] = True
        self.fields['title'].widget.attrs['aria-label'] = 'Review Title'
        self.fields['content'].widget.attrs['aria-label'] = 'Review Content'

        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-black rounded-0'
            self.fields[field].label = False
