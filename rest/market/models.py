from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

#admin password is superuser

@python_2_unicode_compatible
class Restaraunt(models.Model):
#   id = models.IntegerField(primary_key=True)
    type = models.IntegerField(default=0) #0 - unknown, pizza, italian, chinise 
    name = models.CharField(max_length=1024)
    location_hash = models.CharField(max_length=256)
    location_lalo = models.CharField(max_length=256)
    address = models.CharField(max_length=1024)
    money_grade = models.IntegerField(default=0) # 0 - unknown, 1 - chip .. 100 - expensive 
    rating_quality = models.IntegerField(default=0)
    rating_service = models.IntegerField(default=0)
    rating_fast = models.IntegerField(default=0)
    start_time = models.TimeField()
    end_time = models.TimeField()
    minimum_order = models.DecimalField(max_digits=10, decimal_places=2)
    delivery_price = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return u"%s" % self.name
    #money and law fields here

@python_2_unicode_compatible
class Diner(models.Model):
#   id = models.IntegerField(primary_key=True)
    address = models.CharField(max_length=1024)
    def __str__(self):
        return u"%s" % self.address

class Rating(models.Model): #Do we need to store it?
    restaraunt = models.ForeignKey(Restaraunt)
    diner = models.ForeignKey(Diner)
    rating_quality = models.IntegerField(default=0)
    rating_service = models.IntegerField(default=0)
    rating_fast = models.IntegerField(default=0)
    comment = models.CharField(max_length=1024)

@python_2_unicode_compatible
class Dish(models.Model):
#   id = models.IntegerField(primary_key=True)
    restaraunt = models.ForeignKey(Restaraunt)
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=1024,default='')
    type = models.IntegerField() # Pizza,  Pizza margherita
    weight = models.IntegerField() # Weight or something
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rank = models.IntegerField() # popularity
    make_time = models.IntegerField()
    def __str__(self):
        return u"%s" % self.name

class Dish_type(models.Model):
#   id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=256)

    
    
    
    
    
    
    