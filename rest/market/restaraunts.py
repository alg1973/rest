from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Restaraunt


def show (request):
    restaraunts_list = Restaraunt.objects.all()
    template = loader.get_template('market/restaraunts.html')
    context = {
        'restaraunts_list': restaraunts_list,
    }
    return HttpResponse(template.render(context, request))

