from django import forms
from .models import Faq


class FaqForm(forms.ModelForm):
    """
    Add / Edit Faq form
    """

    class Meta:
        model = Faq
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Sets placeholder values
        placeholders = {
            'question': 'Question',
            'answer': 'Answer'
        }

        # Sets autofocus on first input
        self.fields['question'].widget.attrs['autofocus'] = True

        # Sets aria-labels on inputs
        self.fields['question'].widget.attrs['aria-label'] = 'FAQ Question'
        self.fields['answer'].widget.attrs['aria-label'] = 'FAQ Answer'

        for field in self.fields:
            # Sets placeholders on fields with * for required fields
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]

            # Sets placecholders on inputs
            self.fields[field].widget.attrs['placeholder'] = placeholder

            # Adds stylings classes to inputs
            self.fields[field].widget.attrs['class'] = (
                'ib-form-field mb-3 px-2 py-2 font-body text-dark-grey')

            # Removes input labels
            self.fields[field].label = False
