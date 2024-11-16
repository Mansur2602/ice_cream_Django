from django.db import models

class IceCream(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название мороженого')  
    flavor = models.CharField(max_length=50, verbose_name='Вкус мороженого')
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Цена')

    def __str__(self):
        return self.name
