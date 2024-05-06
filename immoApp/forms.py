from django import forms
from .models import estate

class estateForm(forms.ModelForm):
    class Meta:
        model = estate
        fields= ['name', 'living_space','number_rooms', 'has_balcony', 'house_type', 'year_built']