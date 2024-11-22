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
    price = forms.DecimalField( decimal_places=2, label="Цена")
    captcha = CaptchaField()


    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price <= 0:
            raise forms.ValidationError("Цена должна быть больше нуля.")
        if price > 1000:
            raise forms.ValidationError("Цена не может быть больше 1000.")
        
    def clean_flavor(self):
        flavor = self.cleaned_data.get('flavor')
        name = self.cleaned_data.get('name')
        if len(flavor) < 3:
            raise forms.ValidationError("Вкус должен содержать не менее 3 символов.")
        if flavor.lower() == name.lower():
            raise forms.ValidationError("Вкус не может быть одинаковым с названием.")
        return flavor
    

    


