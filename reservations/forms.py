from django import forms

from .models import Reservation

# Allows Form Creation
class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = "__all__"      # All the fields of the Reservation Model
        widgets = {
            "date": forms.DateTimeInput(attrs={"type": "datetime-local"}),      # Converts the data field from simple text type to data-time type
        }