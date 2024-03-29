from django import forms
from .models import Booking, Workshop, DIET
from django.utils.safestring import mark_safe
from datetime import date


# register the Booking model and select which fields to use
class BookingForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Filter the workshops to show only future events
        self.fields['workshop'].queryset = Workshop.objects.filter(
            event_date__gt=date.today()
            )

    class Meta:
        model = Booking
        fields = [
            'workshop', 'name', 'email',
            'phone_number', 'spaces', 'dietary_requirements'
            ]

    # form validation and relevant alerts
    def clean_spaces(self):
        spaces = self.cleaned_data.get('spaces')
        workshop = self.cleaned_data.get('workshop')

        if spaces is None or spaces <= 0:
            raise forms.ValidationError(
                "Please enter a valid number of spaces."
                    )

        if workshop and spaces > workshop.spaces:
            error_message = (
                f'Only <strong>{ workshop.spaces } </strong>'
                f'spaces remain on <br>"{ workshop }"'
            )
            raise forms.ValidationError(mark_safe(error_message))

        return spaces
