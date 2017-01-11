from __future__ import print_function
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.db.models import Count
import sys
import geosort
import auth


from .models import Restaurant, Diner



    


def show (request):
    au = auth.Auth(request)                
    if 'q' in request.GET: #sql inject
        restaurants_list = Restaurant.objects.filter(
            dish__name__icontains=request.GET['q']).annotate(meal=Count('dish'))
    elif 'g' in request.GET:
        point=address2latlng(request.GET['g'])
        restaurants_list = get_restaurants_near_latlng(g['lat'],g['lng'])
    else:
        restaurants_list = Restaurant.objects.all()
    template = loader.get_template('market/restaurants.html')
    context = {
        'auth_list': au.get_list(),
        'restaurants_list': restaurants_list,
    }
    return HttpResponse(template.render(context, request))

def get_restaurants_near_latlng(lat,lng):
    cell_list =  get_cells_of_region(lat,lng)
    return Restaurant.objects.filter(location_cell__in=cell_list)
