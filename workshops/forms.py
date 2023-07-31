from django import forms
from .models import Booking, DIET

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'email', 'phone_number', 'spaces', 'dietary_requirements']

    def clean_spaces(self):
        spaces = self.cleaned_data.get('spaces')
        if spaces <= 0:
            raise forms.ValidationError("Please enter a valid number of spaces.")
        return spaces
