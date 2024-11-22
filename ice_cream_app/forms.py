# from django import forms
# from .models import IceCream

# class IceCreamForm(forms.ModelForm):
#     class Meta:
#         model = IceCream
#         fields = ['name', 'flavor', 'price',] 

#     def clean_price(self):
#         price = self.cleaned_data.get('price')
#         if price <= 0:
#             raise forms.ValidationError("Цена должна быть больше нуля.")
#         return price

from django import forms
from captcha.fields import CaptchaField

class IceCreamForm(forms.Form):
    name = forms.CharField(max_length=100, label="Название")
    flavor = forms.CharField(max_length=100, label="Вкус")
    price = forms.DecimalField(max_digits=5, decimal_places=2, label="Цена")
    captcha = CaptchaField()


    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price <= 0:
            raise forms.ValidationError("Цена должна быть больше нуля.")
        return price
