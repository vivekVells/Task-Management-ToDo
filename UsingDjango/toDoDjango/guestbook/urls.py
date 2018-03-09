from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='gbIndex'),
    path('sign/', views.sign, name='gbSign')
]