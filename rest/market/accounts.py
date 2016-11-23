from __future__ import print_function
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.db.models import Count
import sys
import geocoder
import s2


from .models import Restaraunt
from .models import Dish


def validate_time(str):
    return str


def show (request,rest_id="0"):
    if 'name' in request.GET:
	return edit_restraunt(request,rest_id)
    restaraunt=()
    if int(rest_id): 
        restaraunt = Restaraunt.objects.get(pk=rest_id)
    template = loader.get_template('market/accounts.html')
    context = {
        'restaraunt': restaraunt,
    }
    return HttpResponse(template.render(context, request))

def edit_restraunt(request,rest_id):
    restaraunt={}
    if request.GET.has_key('name') and request.GET.has_key('address'):

        restaraunt['name']=request.GET['name']
        restaraunt['address']=request.GET['address']

        r=Restraraunt(name=restaraunt['name'],
                      address=restaraunt['address'])
# yandex geocoder lang='ru-RU', google geocoder language='ru'
	geo=geocoder.yandex(request.GET['address'],lang='ru')
        
        r.location_lat=geo.lat
        r.location_lng=geo.lng
	restaraunt['location_lat']=geo.lat
	restaraunt['location_lng']=geo.lng

        latlng = s2.S2LatLng.FromDegrees(float(geo.lat), 
                                         float(geo.lng))
        cell = s2.S2CellId.FromLatLng(latlng).parent(14)

        r.location_hash=cell.id
        restaraunt['location_hash']=cell.id

        if request.GET.has_key('start'):
            r.start_time=validate_time(request.GET['start'])
            restaraunt['start_time']=r.start_time

        if request.GET.has_key('end'):
            r.end_time=validate_time(request.GET['end'])
            restaraunt['end_time']=r.end_time
         
        if request.GET.has_key('morder'):
            r.minumum_order=request.GET['morder']
            restaraunt['minimum_order']=request.GET['morder']
        if request.GET.has_key('dprice'):
            r.delivery_price=request.GET['delivery_price']
            restaraunt['delivery_price']=request.GET['delivery_price']
    else:
	print (request.GET,sys.stderr)
	restaraunt['name']='Error'

    template = loader.get_template('market/accounts.html')
    context = {
        	'restaraunt': restaraunt,
    }
    return HttpResponse(template.render(context, request))
	

