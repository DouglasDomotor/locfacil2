from django import forms
from .models import Car

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['model', 'plate', 'year', 'km', 'status', 'purchase_price', 'financed']
