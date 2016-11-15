from django.shortcuts import render
from django.http import HttpResponse



def show (request,rest_id):
    return HttpResponse("Restaraunt %s menu will be there." % rest_id)
