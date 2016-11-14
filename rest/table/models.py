
from django.db import models

class Restaraunt(models.Model):
    id = models.IntegerField(primary_key=True)
    type = models.IntegerField(default=0) #0 - unknown, pizza, italian, chinise 
    name = models.CharField(max_len=1024)
    location_hash = models.CharField(max_len=256)
    location_lalo = models.CharFieled(max_len=256)
    address = models.CharField(max_len=1024)
    money_grade = models.IntegerField(default=0) # 0 - chip, 100 - expensive 
    rating_quality = models.IntegerField(default=0)
    rating_service = models.IntegerField(default=0)
    rating_fast = models.IntegerField(default=0)
    start_time = models.DateField()
    end_time = models.DateField()
    minimum_order = models.NumberField()
    delivery_price = models.NumberField()
    #money and law fields here

class Rating(models.Model): #Do we need to store it?
    restaraunt_id = models.ForeignKey(Restaraunt)
    diner_id = models.ForeignKey(Diner)
    rating_quality = models.IntegerField(default=0)
    rating_service = models.IntegerField(default=0)
    rating_fast = models.IntegerField(default=0)
    comment = models.CharField(max_len=1024)

class Dish
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_len=256)
    type = models.IntegerField() # Pizza,  Pizza margеrita
    weight = models.IntegerField() # Weight or something
    price = models.NumberField()
    rank = models.IntegerField() # popularity
    make_time = models.IntegerField()
    
    
    
    
    
    
