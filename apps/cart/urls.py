#!/user/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.urls import re_path

from . import views

app_name = 'cart'

urlpatterns = [
    re_path(r'^$', views.user_cart, name="cart"),
    re_path(r'^add(\d+)_(\d+)/$', views.add, name="add"),
    re_path(r'^edit(\d+)_(\d+)/$', views.edit, name="edit"),
    re_path(r'^delete(\d+)/$', views.delete, name="delete"),
]
