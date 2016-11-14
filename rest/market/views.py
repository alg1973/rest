from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Restaurants list will be there.")

# Create your views here.
