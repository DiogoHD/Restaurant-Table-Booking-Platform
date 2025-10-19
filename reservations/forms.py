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
        labels = {
            "name": "Nome e Apelido",
            "phone_number": "Telemóvel",
            "date": "Data e Hora",
            "guests": "Número Total de Pessoas",
            "table": "Mesa (Opcional)",
            "notes": "Notas",
        }
    
    # Constructor Method (Called every time we create an instance)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)           # The parent class (forms.ModelForm) initializes everything by default
        for name, field in self.fields.items():     # Dictionary with every field on the forms
            # Adds attributes to the field
            field.widget.attrs.update({
                'class': 'form-control',            # Applies a style to the 
                'placeholder': field.label,     
            })   