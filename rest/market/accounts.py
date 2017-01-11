from __future__ import print_function
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.db.models import Count
from django.db import connection

import sys
import geocoder
import s2
import geosort
import decimal
import time
from datetime import datetime


from .models import Restaurant
from .models import Dish




def show (request,rest_id="0"):
    return edit_restaurant(request,rest_id)

def validate_tel(tel):
    return tel

def validate_time(t):
    return datetime.strptime(t,"%H:%M")



def set_address_s2cell(db_rec,address):
    db_rec.address=address
    g=geosort.address2latlng(address)
    
    db_rec.location_lat=decimal.Decimal(g['lat'])
    db_rec.location_lng=decimal.Decimal(g['lng'])
    
    db_rec.location_cell=geosort.latlng2sell(g)


def show_result(request, restaurant_db, restaurant_attr):
    template = loader.get_template('market/accounts.html')
    context = {
        'restaurant': restaurant_db,
        'restaurant_attr': restaurant_attr,
    }
    return HttpResponse(template.render(context, request))
    


def edit_restaurant(request,rest_id):
    restaurant_db=() # db record
    restaurant_attr={}

    if int(rest_id): #show start form for edit
        restaurant_db = Restaurant.objects.get(pk=rest_id)
        restaurant_attr['edit_id']=rest_id
        return show_result(request,restaurant_db,restaurant_attr)

    if request.GET.has_key('edit_id'): #It's edit result

        restaurant_db = Restaurant.objects.get(pk=request.GET['edit_id'])
       

        if  request.GET.has_key('name'):
            restaurant_db.name = request.GET['name']
#we can change lat-lng and cell only from address
        if  request.GET.has_key('address'): 
            set_address_s2cell(restaurant_db,request.GET['address'])
        if request.GET.has_key('start'):
            restaurant_db.start_time=validate_time(request.GET['start'])
        if request.GET.has_key('end'):
            restaurant_db.end_time=validate_time(request.GET['end'])
        if request.GET.has_key('morder'):
            restaurant_db.minimum_order=decimal.Decimal(request.GET['morder'])
        if request.GET.has_key('dprice'):
            restaurant_db.delivery_price=decimal.Decimal(request.GET['dprice'])

    elif request.GET.has_key('name') and request.GET.has_key('address'): #create new one 
        
        restaurant_db=Restaurant(name=request.GET['name'])
        set_address_s2cell(restaurant_db,request.GET['address'])

        
        restaurant_db.start_time=validate_time(request.GET.get('start',
                                                               default="09:00"))
        restaurant_db.end_time=validate_time(request.GET.get('end',
                                                             default="23:00"))
        restaurant_db.minimum_order=decimal.Decimal(request.GET.get('morder',
                                                                    default="0.0"))
        restaurant_db.delivery_price=decimal.Decimal(request.GET.get('dprice',
                                                                     default="0.0"))

    else: # default we should show error here if no name and address 
        restaurant_db={ 'start_time' : datetime.strptime("09:00","%H:%M"),
                        'end_time' : datetime.strptime("23:00","%H:%M"),
                        'minimum_order' : "0.0",
                        'delivery_price' : "0.0" }
        return show_result(request,restaurant_db,restaurant_attr)  


    if request.GET.has_key('tel'):
        restaurant_db.tel=validate_tel(request.GET['tel'])
    
    restaurant_db.save()
    #after the save() we have id.

    restaurant_attr['edit_id']=restaurant_db.id 
    #print (connection.queries,sys.stderr)
    return show_result(request,restaurant_db,restaurant_attr)   
	

