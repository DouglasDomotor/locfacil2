from django import forms
from .models.cars import Car

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['model', 'plate', 'year', 'km', 'status', 'purchase_price', 'financed']
        labels = {
            'model': 'Modelo',
            'plate': 'Placa',
            'year': 'Ano',
            'km': 'Quilometragem',
            'status': 'Status',
            'purchase_price': 'Valor de compra',
            'financed': 'Financiado',
        }        
        
