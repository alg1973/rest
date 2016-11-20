from __future__ import print_function
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.db.models import Count
import sys
import geocoder


from .models import Restaraunt
from .models import Dish

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
    if request.GET.has_key('lat') and request.GET.has_key('lng'):
	geo=geocoder.yandex([request.GET['lat'],
			request.GET['lng']],method="reverse")
        restaraunt['address']=geo.address
	restaraunt['latlng']=geo.latlng
	restaraunt['name']=request.GET['name']
    else:
	print (request.GET,sys.stderr)
	restaraunt['name']='Error'

    template = loader.get_template('market/accounts.html')
    context = {
        	'restaraunt': restaraunt,
    }
    return HttpResponse(template.render(context, request))
	

