from django.http import HttpResponse
from django.utils import timezone


from .models import Dish,Restaraunt,Diner,Basket,BasketEntry

import auth
import sys

class Bsk:
    basket_list = {}

    def __init__(self, au, request):
        self.auth=au

    def empty(self):
        self.load()
        return len(self.dishes)<=0

    def load(self):
        try: 
            self.basket = Basket.objects.get(diner=self.auth.diner())
            self.dishes = self.basket.dishes.all()
            if len(self.dishes)>0:
                self.restaraunt_id = self.dishes[0].restaraunt.id
            else:
                self.restaraunt_id = 0
        except Basket.DoesNotExist:
            self.basket = Basket(diner=self.auth.diner())
            self.basket.save()
#        self.dish_list = basket.dishes.all()

    def add_2basket(self,request):
        if 'dish_id' in request.GET:
            if request.GET.get('q',0)!=0:
                self.load()
                meal = Dish.objects.get(pk=request.GET['dish_id'])
                if self.empty() or (self.restaraunt_id == meal.restaraunt.id):
                    try:
                        basket_ent = BasketEntry.objects.get(dish=meal,basket=self.basket)
                        basket_ent.quantity+=int(request.GET['q'])
                    except BasketEntry.DoesNotExist:
                        basket_ent = BasketEntry(dish=meal,basket=self.basket)
                        basket_ent.quantity=request.GET['q']

                    basket_ent.change_date=timezone.now()
                    basket_ent.save()
                   
                        
            else:
                    self.auth.message("Cant add meal to basket from other restaraunt")



        
