from django.http import HttpResponse


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
                self.basket.dishes.create(dish=request.GET['dish_id'],
                                          quantity=request.GET['q'])
                self.basket.save()



        
