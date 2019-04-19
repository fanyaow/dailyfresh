from django.shortcuts import render

# Create your views here.
from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'order'

urlpatterns = [
    path('', views.order, name="order"),
    path('push/', views.order_handle, name="push"),
]