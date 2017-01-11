import restaurants
import menus
import accounts
import bskorder
import order

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return restaurants.show(request)

def menu(request,rest_id):
    return menus.show(request,rest_id)

def account(request,rest_id="0"):
    return accounts.show(request,rest_id)

def basket(request):
    return bskorder.show(request)


def checkout(request):
    return order.show(request)

# Create your views here.
