from django import forms
from .models import Exhibit


class ExhibitForm(forms.ModelForm):
    class Meta:
        model = Exhibit
        fields = ['date', 'planet'] # planets is limited ot breakfast, lunch, dinner as it was on models.py
        widgets = {
            'date': forms.DateInput( # Turns date into a proper date field
                format=('%Y-%m-%d'),
                attrs={
                    'placeholder': 'Select a date',
                    'type': 'date'
                }
            ),
        }