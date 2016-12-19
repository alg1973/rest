from __future__ import print_function
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.db.models import Count
from django.db import connection

from .models import Restaraunt, Diner, OrderDishes, Order
from .models import Dish, Basket, BasketEntry


import auth
import sys
import basket

def show (request):
    au = auth.Auth(request)
    bsk = basket.Bsk(au,request)
    if 'login' in request.GET:
        au.upgrade_diner(request)
    if 'payment_type' in request.GET:
        order_list = process_order(au,bsk,request)

    template = loader.get_template('market/order.html')
    context = {
        'auth_list': au.get_list(),
        'dish_list': bsk.dish_list(),
        'restaraunt': bsk.restraunt(),
    }
    return HttpResponse(template.render(context, request))





