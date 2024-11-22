from django.shortcuts import render, redirect
from .forms import IceCreamForm
from .models import IceCream

def create_ice_cream(request):
    if request.method == 'POST':
        form = IceCreamForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            flavor = form.cleaned_data['flavor']
            price = form.cleaned_data['price']
            ice_cream = IceCream(name=name, flavor=flavor, price=price)
            ice_cream.save()
            return render(request, 'ice_cream_app/success.html', {'message': 'Мороженое успешно добавлено!'})
        else:
            return render(request, 'ice_cream_app/create_ice_cream.html', {'form': form, 'message': 'Ошибка валидации, пожалуйста, исправьте данные.'})
    else:
        form = IceCreamForm()

    return render(request, 'ice_cream_app/create_ice_cream.html', {'form': form})


def ice_cream_list(request):
  
    ice_creams = IceCream.objects.all()

    return render(request, 'ice_cream_app/ice_cream_list.html', {'ice_creams': ice_creams})


