from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.guestbookIndex, name='index'),
    path('sign/', views.guestbookSign, name='sign')
]