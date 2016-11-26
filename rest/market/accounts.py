from __future__ import print_function
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.db.models import Count

import sys
import geocoder
import s2
import decimal
import time
from datetime import datetime


from .models import Restaraunt
from .models import Dish




def show (request,rest_id="0"):
    return edit_restaraunt(request,rest_id)

def validate_tel(tel):
    return tel

def validate_time(t):
    return datetime.strptime(t,"%H:%M")

def address2latlng(address):
    # yandex geocoder lang='ru-RU', google geocoder language='ru'
    geo=geocoder.yandex(address,lang='ru')
    return dict([('lat',decimal.Decimal(geo.lat)),('lng',decimal.Decimal(geo.lng))])


def edit_restaraunt(request,rest_id):
    restaraunt_db=() # db record
    restaraunt_attr={}

    if int(rest_id): #edit 
        restaraunt_db = Restaraunt.objects.get(pk=rest_id)
        restaraunt_attr['edit_id']=rest_id

    elif request.GET.has_key('name') and request.GET.has_key('address'): #create new one 

        restaraunt_db=Restaraunt(name=request.GET['name'],
                      address=request.GET['address'])

	g=address2latlng(restaraunt_db.address)
        
        restaraunt_db.location_lat=g['lat']
        restaraunt_db.location_lng=g['lng']

        latlng = s2.S2LatLng.FromDegrees(float(g['lat']), 
                                         float(g['lng']))
        cell = s2.S2CellId.FromLatLng(latlng).parent(14)

        restaraunt_db.location_cell=cell.id()
        
        restaraunt_db.start_time=validate_time(request.GET.get('start',default="09:00"))
        restaraunt_db.end_time=validate_time(request.GET.get('end',default="23:00"))
        restaraunt_db.minimum_order=decimal.Decimal(request.GET.get('morder',default="0.0"))
        restaraunt_db.delivery_price=decimal.Decimal(request.GET.get('dprice',default="0.0"))

        if request.GET.has_key('tel'):
            restaraunt_db.tel=validate_tel(request.GET['tel'])
  
        restaraunt_db.save()
    else: # default 
        restaraunt_db={ 'start_time' : datetime.strptime("09:00","%H:%M"),
                        'end_time' : datetime.strptime("23:00","%H:%M"),
                        'minimum_order' : "0.0",
                        'delivery_price' : "0.0" }
 
   

    template = loader.get_template('market/accounts.html')
    context = {
        	'restaraunt': restaraunt_db,
    }
    return HttpResponse(template.render(context, request))
	

