
from django.urls import path
from .views import create_ice_cream, ice_cream_list

urlpatterns = [
    path('', ice_cream_list, name='ice_cream_list'),
    path('create/', create_ice_cream, name='create_ice_cream'),
   
]
