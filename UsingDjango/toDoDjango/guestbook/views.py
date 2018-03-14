from django.shortcuts import render
from django.http import HttpResponse

def guestbookView(request):
    return HttpResponse('Guestbook View!!!')

def guestbookIndex(request):
    return render(request, 'guestbook/index.html')

def guestbookSign(request):
    return render(request, 'guestbook/sign.html')