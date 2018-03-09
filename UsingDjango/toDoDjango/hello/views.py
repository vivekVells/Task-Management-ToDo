from django.shortcuts import render

# http resonspe
from django.http import HttpResponse

def index(request):
    return HttpResponse('Reponse obtained...\nWelcome to Django World!!!')