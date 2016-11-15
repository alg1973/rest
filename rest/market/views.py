import restaraunts
import menus

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return restaraunts.show(request)

def menu(request,rest_id):
    return menus.show(request,rest_id)

# Create your views here.
