from django import forms
from django.contrib.auth.models import User
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)

        # Sets placeholder values for form inputs
        placeholders = {
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_town_or_city': 'Town or City',
            'default_county': 'County, State or Locality',
            'default_postcode': 'Postal Code',
            'default_phone_number': 'Phone Number',
        }

        # Sets autofocus on first input
        self.fields['default_street_address1'].widget.attrs['autofocus'] = True

        for field in self.fields:
            # Adds placeholders to inputs (except Country)
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder

            # Adds styling classes to all inputs
            self.fields[field].widget.attrs['class'] = (
                    'ib-form-field mb-3 px-2 py-2 font-body text-dark-grey')

            # Removes labels from inputs
            self.fields[field].label = False


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name')

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes,
        remove auto-generated labels
        """
        super().__init__(*args, **kwargs)

        # Sets placeholder values for form inputs
        placeholders = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
        }

        for field in self.fields:
            # Adds placeholders to inputs (except Country)
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder

            # Adds styling classes to all inputs
            self.fields[field].widget.attrs['class'] = (
                    'ib-form-field mb-3 px-2 py-2 font-body text-dark-grey')

            # Removes labels from inputs
            self.fields[field].label = False
