from __future__ import print_function
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.db.models import Count
import sys
import geosort
import auth


from .models import Restaraunt, Diner



    


def show (request):
    auth_list= auth.check(request)
                
    if 'q' in request.GET: #sql inject
        restaraunts_list = Restaraunt.objects.filter(
            dish__name__icontains=request.GET['q']).annotate(meal=Count('dish'))
    elif 'g' in request.GET:
        point=address2latlng(request.GET['g'])
        restaraunts_list = get_restaraunts_near_latlng(g['lat'],g['lng'])
    else:
        restaraunts_list = Restaraunt.objects.all()
    template = loader.get_template('market/restaraunts.html')
    context = {
        'auth_list': auth_list,
        'restaraunts_list': restaraunts_list,
    }
    return HttpResponse(template.render(context, request))

def get_restaraunts_near_latlng(lat,lng):
    cell_list =  get_cells_of_region(lat,lng)
    return Restaraunt.objects.filter(location_cell__in=cell_list)
