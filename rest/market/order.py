# -*- coding: utf-8 -*-
from __future__ import print_function
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.db.models import Count
from django.db import connection

from .models import Restaurant, Diner, OrderDishes, Order
from .models import Dish, Basket, BasketEntry



import datetime
import auth
import sys
import basket

def show (request):
    au = auth.Auth(request)
    order_list = show_order(au,request)

    template = loader.get_template('market/order.html')
    context = {
        'auth_list': au.get_list(),
        'order_list': order_list
    }
    return HttpResponse(template.render(context, request))


def calculate_total(dish_list,restaurant):
    total = 0
    for meal in dish_list:
        total += meal.quantity*meal.dish.price
    total += restaurant.delivery_price
    return total

def check_order_validity(ord_list,restraunt):
    if restraunt.minimum_order and ord_list['total']<restraunt.minimum_order:
        ord_list['valid'] = 0
        ord_list['message'] = 'Сумма меньше минимального заказа, добавьте еще'
    if restraunt.start_time<restraunt.end_time:
        restaurant_now=(datetime.datetime.utcnow()+
                  datetime.timedelta(seconds=restraunt.tz_offset)).time()
        if  restaurant_now<restraunt.start_time or restaurant_now>restraunt.end_time:
            ord_list['valid'] = 0
            ord_list['message'] = 'Ресторан сейчас не работает, приходите позже???'

def show_order(au,request):
    bsk = basket.Bsk(au,request)
    ord_list = {}
    ord_list ['dish'] = bsk.dish_list()
    ord_list ['restaurant'] = bsk.restaurant()
    ord_list ['address'] = au.diner().address
    ord_list ['tel'] = au.diner().tel
    ord_list ['email'] = au.diner().email
    ord_list ['dprice'] = bsk.restaurant().delivery_price
    ord_list ['total'] = calculate_total(bsk.dish_list(),bsk.restaurant())
    return  check_order_validity(ord_list,bsk.restraunt())
        




