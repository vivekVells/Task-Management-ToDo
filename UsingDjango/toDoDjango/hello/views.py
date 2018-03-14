from django.shortcuts import render

from django.http import HttpResponse

def welcomeMessage(request):
    return HttpResponse('Welcome to Django World!')