
from django.urls import path
from .views import create_ice_cream, ice_cream_list, ice_cream_search

urlpatterns = [
    path('', ice_cream_list, name='ice_cream_list'),
    path('create/', create_ice_cream, name='create_ice_cream'),
    path('search/', ice_cream_search )
   
]
