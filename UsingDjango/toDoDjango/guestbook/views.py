from django.shortcuts import render
from .models import Comment

def index(request):
    commentObj = Comment.objects
    return render(request, 'guestbook/index.html', commentObj)

def sign(request):
    return render(request, 'guestbook/sign.html')