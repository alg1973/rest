from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.utils import timezone


from .models import Dish,Restaurant,Diner,Basket,BasketEntry

import auth
import sys
import basket


def show (request):
    au = auth.Auth(request)
    bsk = basket.Bsk(au,request)
    bsk.update_bsk(request)
    template = loader.get_template('market/basket.html')
    context = {
        'auth_list': au.get_list(),
        'dish_list': bsk.dish_list(),
        'restaurant': bsk.restaurant(),
    }
    return HttpResponse(template.render(context, request))

