from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse('страница приложения пловцы')
# Create your views here.
