from django.shortcuts import render, redirect
from .forms import IceCreamForm, FormIceCreamSearch
from .models import IceCream
from django.core.paginator import Paginator, Page

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
    paging = Paginator( ice_creams,per_page=10,orphans=0, allow_empty_first_page=True )
    num_page = 1
    if 'page' in request.GET:
        num_page = request.GET['page']    
    page = paging.page( num_page )


    return render(request, 'ice_cream_app/ice_cream_list.html', {'page' : page, 'ice_creams': ice_creams})





def ice_cream_search(request):
    ice_creams = []
    form = FormIceCreamSearch(request.POST)  


    if form.is_valid():
        search_name = form.cleaned_data['name']

        ice_creams = IceCream.objects.filter(name=search_name)

    return render(request, 'ice_cream_app/ice_cream_search.html', {
        'form': form,
        'ice_creams': ice_creams,
    })




