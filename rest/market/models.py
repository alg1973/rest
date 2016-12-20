from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

#admin password is superuser


class Restaraunt(models.Model):
#   id = models.IntegerField(primary_key=True)
    type = models.IntegerField(default=0) #0 - unknown, pizza, italian, chinise 
    name = models.CharField(max_length=1024,db_index=True)
    location_cell = models.BigIntegerField(db_index=True) #s2 cell level 14
    location_lat =   models.DecimalField(max_digits=10, decimal_places=6)
    location_lng = models.DecimalField(max_digits=10, decimal_places=6)
    address = models.CharField(max_length=1024)
    money_grade = models.IntegerField(default=0) # 0 - unknown, 1 - chip .. 100 - expensive 
    rating_quality = models.IntegerField(default=0)
    rating_service = models.IntegerField(default=0)
    rating_fast = models.IntegerField(default=0)
    start_time = models.TimeField()
    end_time = models.TimeField()
    minimum_order = models.DecimalField(max_digits=10, decimal_places=2)
    delivery_price = models.DecimalField(max_digits=10, decimal_places=2)
    tel = models.CharField(max_length=15)
    open_orders =  models.IntegerField(default=0)
    tz_offset = models.IntegerField(default=0)
    # restraunt identification staff
    pin = models.CharField(max_length=5)
    email = models.CharField(max_length=128,db_index=True)
    password =  models.CharField(max_length=128)
    def __unicode__(self):
        return u"%s" % self.name
    class Meta:
        unique_together = (("name","address"),)
    
    #money and law fields here


class Dish(models.Model):
    restaraunt = models.ForeignKey(Restaraunt)
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=1024,default='')
    type = models.IntegerField() # Pizza,  Pizza margherita
    weight = models.IntegerField() # Weight or something
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rank = models.IntegerField() # popularity
    make_time = models.IntegerField()
    def __unicode__(self):
        return u"%s" % self.name


class Diner(models.Model):
    address = models.CharField(max_length=1024)
    login = models.CharField(max_length=64,unique=True)
    password =  models.CharField(max_length=128)
    utype = models.IntegerField() #0 - anonymous session, 1 - register user 
    tel = models.CharField(max_length=15)
    email = models.CharField(max_length=256)
    def __unicode__(self):
        return u"%s" % self.address

class Basket(models.Model):
    diner =  models.ForeignKey(Diner)
    deleted = models.IntegerField(default=0)
    dishes = models.ManyToManyField(Dish, through='BasketEntry')

class BasketEntry(models.Model):
    dish = models.ForeignKey(Dish)
    basket = models.ForeignKey(Basket)
    quantity =  models.IntegerField()
    change_date = models.DateField()

class Order(models.Model):
    diner = models.ForeignKey(Diner)
    restaraunt = models.ForeignKey(Restaraunt)
    state = models.IntegerField()
    dinertel = models.CharField(max_length=15)
    address = models.CharField(max_length=1024)
    location_lat =   models.DecimalField(max_digits=10, decimal_places=6)
    location_lng = models.DecimalField(max_digits=10, decimal_places=6)
    payment_type = models.IntegerField()
    payment_info = models.CharField(max_length=1024)
    diner_comment = models.CharField(max_length=1024)
    restaraunt_comment = models.CharField(max_length=1024)
    change_date = models.DateField()
    changelog =  models.CharField(max_length=4096)
    dishes = models.ManyToManyField(Dish, through='OrderDishes')


class OrderDishes(models.Model):
    dish = models.ForeignKey(Dish)
    order = models.ForeignKey(Order)
    quantity =  models.IntegerField()
    rating = models.IntegerField()




    

class Rating(models.Model): #Do we need to store it?
    restaraunt = models.ForeignKey(Restaraunt)
    diner = models.ForeignKey(Diner)
    rating_quality = models.IntegerField(default=0)
    rating_service = models.IntegerField(default=0)
    rating_fast = models.IntegerField(default=0)
    comment = models.CharField(max_length=1024)




class Dish_type(models.Model):
    name = models.CharField(max_length=256)
    dtype = models.IntegerField()


    
    
