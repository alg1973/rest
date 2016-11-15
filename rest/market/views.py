import restaraunts
import menu

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return restataunts.show(request)

def menu(request,rest_id):
    return menu.show(request,rest_id)

# Create your views here.
