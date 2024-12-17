import random
from decimal import Decimal
from .models import IceCream


names = [
"Шоколадное", "Ванильное", "Клубничное", "Молочное",
   
]


flavors = [
    "Смородиновое", "Карамельное", "Тортилья", "Манговое", "Пломбир", "Мятное", "Персиковое"
]

def generate_random_ice_cream(n):
    
    for _ in range(n):
        name = random.choice(names) 
        flavor = random.choice(flavors)  
        price = round(random.uniform(10, 1000), 2)  
        ice_cream = IceCream(name=name, flavor=flavor, price=Decimal(price))
        ice_cream.save()


