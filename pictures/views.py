# from django.shortcuts import render
import datetime as dt
from django.http import HttpResponse

# Create your views here.
def welcome(request):
    return HttpResponse('welcome to the art gallery')
