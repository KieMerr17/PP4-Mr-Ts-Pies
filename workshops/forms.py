from django import forms
from .models import Booking, Workshop, DIET
from django.utils.safestring import mark_safe

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['workshop', 'name', 'email', 'phone_number', 'spaces', 'dietary_requirements']

    def clean_spaces(self):
        spaces = self.cleaned_data.get('spaces')
        workshop = self.cleaned_data.get('workshop')

        if spaces is None or spaces <= 0:
            raise forms.ValidationError("Please enter a valid number of spaces.")

        if workshop and spaces > workshop.spaces:
            raise ValidationError(mark_safe(f'<strong>{ workshop.spaces }</strong> spaces remaining. '))

        return spaces

