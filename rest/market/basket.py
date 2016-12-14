from django.http import HttpResponse
from django.utils import timezone


from .models import Dish,Restaraunt,Diner,Basket,BasketEntry


import auth

class Bsk:
    basket_list = {}

    def __init__(self, au, request):
        self.auth=au
    
    def load(self):
        try: 
            self.basket = Basket.objects.get(diner=self.auth.diner())
        except Basket.DoesNotExist:
            self.basket = Basket(diner=self.auth.diner())
            self.basket.save()
#        self.dish_list = basket.dishes.all()

    def add_2basket(self,request):
        if 'dish_id' in request.GET:
            if request.GET.get('q',0)!=0:
                self.load()
                meal = Dish.objects.get(pk=request.GET['dish_id'])
                basket_ent = BasketEntry(dish=meal,basket=self.basket)
                basket_ent.quantity=request.GET['q']
                basket_ent.change_date=timezone.now()
                #self.basket.dishes.add(basket_ent)
                basket_ent.save()
                self.basket.save()



        
