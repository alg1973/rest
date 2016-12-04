from __future__ import print_function
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.db.models import Count
import sys
import geosort


from .models import Restaraunt



    


def show (request):
    if 'q' in request.GET: #sql inject
        restaraunts_list = Restaraunt.objects.filter(
            dish__name__icontains=request.GET['q']).annotate(meal=Count('dish'))
    elif 'g' in request.GET:
        cellid=geo2cell(request.GET['g'])
        restaraunts_list = get_restaraunts_near_cell(cellid)
    else:
        restaraunts_list = Restaraunt.objects.all()
    template = loader.get_template('market/restaraunts.html')
    context = {
        'restaraunts_list': restaraunts_list,
    }
    return HttpResponse(template.render(context, request))

