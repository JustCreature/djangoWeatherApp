from django import forms
from .models import City

class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = [
            'name',
        ]

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'name': 'city',
                'id': 'city',
                'placeholder': 'Enter your city',
            })
        }