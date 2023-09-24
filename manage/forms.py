from django import forms
from .models import Message


class MessageForm(forms.ModelForm):
    """
    Form for Message Model
    """

    class Meta:
        model = Message
        fields = ('name', 'email', 'subject', 'content')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Sets placeholder values
        placeholders = {
            'name': 'Your Name',
            'email': 'Your Email',
            'subject': 'Message Subject',
            'content': 'Your Message',
        }

        # Sets autofocus on first input
        self.fields['name'].widget.attrs['autofocus'] = True

        # Sets aria-labels on inputs
        self.fields['name'].widget.attrs['aria-label'] = 'Your Name'
        self.fields['email'].widget.attrs['aria-label'] = 'Your Email'
        self.fields['subject'].widget.attrs['aria-label'] = 'Message Subject'
        self.fields['content'].widget.attrs['aria-label'] = 'Your Message'

        for field in self.fields:
            # Sets placeholders on fields with * for required fields
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]

            # Sets placeholders on inputs
            self.fields[field].widget.attrs['placeholder'] = placeholder

            # Adds stylings classes to inputs
            self.fields[field].widget.attrs['class'] = (
                'ib-form-field mb-3 px-2 py-2 font-body text-dark-grey')

            # Removes input labels
            self.fields[field].label = False
