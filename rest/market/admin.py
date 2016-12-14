from __future__ import unicode_literals
from django.contrib import admin
from .models import Restaraunt, Diner, Rating, Dish, Basket, BasketEntry

admin.site.register(Restaraunt)
admin.site.register(Diner)
admin.site.register(Rating)
admin.site.register(Dish)
admin.site.register(Basket)
admin.site.register(BasketEntry)

# Register your models here.
