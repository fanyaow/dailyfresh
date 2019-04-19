from django.conf.urls import url
from django.urls import path, re_path

from .views import *

app_name = 'user'

urlpatterns = [
    path('register/', register, name="register"),
    path('register_handle/', register_handle, name="register_handle"),
    path('register_exist/', register_exist, name="register_exist"),
    path('login/', login, name="login"),
    path('login_handle/', login_handle, name="login_handle"),
    path('info/', info, name="info"),
    re_path(r'^order/(\d+)$', order, name="order"),
    path('site/', site, name="site"),
    path('logout/', logout, name="logout"),
]