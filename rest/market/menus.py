from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Dish
from .models import Restaurant

import auth
import basket


def show (request,rest_id):
    au = auth.Auth(request)
    bsk = basket.Bsk(au,request)
    bsk.add_2basket(request)
    rest =  Restaurant.objects.get(pk=rest_id)
    menu_list = Dish.objects.filter(restaurant=rest_id)
    template = loader.get_template('market/menus.html')
    context = {
        'auth_list': au.get_list(),
        'menu_list': menu_list,
        'restaurant': rest,
    }
    return HttpResponse(template.render(context, request))
