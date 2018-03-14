from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcomeMessage, name='welcome')
]