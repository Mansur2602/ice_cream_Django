from django import forms
from .models import IceCream

class IceCreamForm(forms.ModelForm):
    class Meta:
        model = IceCream
        fields = ['name', 'flavor', 'price',] 

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price <= 0:
            raise forms.ValidationError("Цена должна быть больше нуля.")
        return price
