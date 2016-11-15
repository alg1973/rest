from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Dish
from .models import Restaraunt


def show (request,rest_id):
    rest =  Restaraunt.objects.get(pk=rest_id)
    menu_list = Dish.objects.filter(restaraunt=rest_id)
    template = loader.get_template('market/menus.html')
    context = {
        'menu_list': menu_list,
        'restaraunt': rest,
    }
    return HttpResponse(template.render(context, request))
