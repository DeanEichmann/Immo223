from django import forms
from .models import Estate

class EstateForm(forms.ModelForm):
    class Meta:
        model = Estate
        fields= ['name', 'address', 'living_space','number_rooms', 'has_balcony', 'house_type', 'year_built']