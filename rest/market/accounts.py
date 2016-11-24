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


def validate_time(str):
    return str


def show (request,rest_id="0"):
    if 'name' in request.GET:
	return edit_restaraunt(request,rest_id)
    restaraunt=()
    if int(rest_id): 
        restaraunt = Restaraunt.objects.get(pk=rest_id)
    template = loader.get_template('market/accounts.html')
    context = {
        'restaraunt': restaraunt,
    }
    return HttpResponse(template.render(context, request))


def validate_tel(tel):
    return tel

def validate_time(t):
    return datetime.strptime(t,"%H:%M")

def address2latlng(address):
    # yandex geocoder lang='ru-RU', google geocoder language='ru'
    geo=geocoder.yandex(address,lang='ru')
    return dict([('lat',decimal.Decimal(geo.lat)),('lng',decimal.Decimal(geo.lng))])


def edit_restaraunt(request,rest_id):
    restaraunt={}
    if request.GET.has_key('name') and request.GET.has_key('address'):

        restaraunt['name']=request.GET['name']
        restaraunt['address']=request.GET['address']

        r=Restaraunt(name=restaraunt['name'],
                      address=restaraunt['address'])

	g=address2latlng(restaraunt['address'])
        
        r.location_lat=g['lat']
        r.location_lng=g['lng']
	restaraunt['location_lat']=float(g['lat'])
	restaraunt['location_lng']=float(g['lng'])

        latlng = s2.S2LatLng.FromDegrees(float(g['lat']), 
                                         float(g['lng']))
        cell = s2.S2CellId.FromLatLng(latlng).parent(14)

        r.location_cell=cell.id()
        restaraunt['location_cell']=cell.id()

        if request.GET.has_key('start'):
            r.start_time=validate_time(request.GET['start'])
            restaraunt['start_time']=r.start_time

        if request.GET.has_key('end'):
            r.end_time=validate_time(request.GET['end'])
            restaraunt['end_time']=r.end_time
         
        if request.GET.has_key('morder'):
            r.minimum_order=decimal.Decimal(request.GET['morder'])
            restaraunt['minimum_order']=request.GET['morder']

        if request.GET.has_key('dprice'):
            r.delivery_price=decimal.Decimal(request.GET['dprice'])
            restaraunt['delivery_price']=request.GET['dprice']
        if request.GET.has_key('tel'):
            r.tel=validate_tel(request.GET['tel'])
            restaraunt['tel']=r.tel
  
        r.save()
    else:
	print (request.GET,sys.stderr)
	restaraunt['name']='Error'

    template = loader.get_template('market/accounts.html')
    context = {
        	'restaraunt': restaraunt,
    }
    return HttpResponse(template.render(context, request))
	

