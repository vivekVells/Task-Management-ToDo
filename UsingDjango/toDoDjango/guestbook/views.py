from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import Comment
from . forms import CommentForms

def guestbookView(request):
    return HttpResponse('Guestbook View!!!')

def guestbookIndex(request):
    commentObj = Comment.objects.order_by('-date_added')
    context = {'comments' : commentObj}
    return render(request, 'guestbook/index.html', context)

def guestbookSign(request):
    if request.method == 'POST':
        form = CommentForms(request.POST)

        if form.is_valid():
            new_comment = Comment(name=request.POST['name'], comment=request.POST['comment'])
            new_comment.save()
            # redirect('view's name)
            return redirect('index')
    else:
        form = CommentForms()
        comForm = CommentForms()
    context = {'form' : comForm}
    return render(request, 'guestbook/sign.html', context)