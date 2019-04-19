"""dailyfresh URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve

import xadmin
from dailyfresh.settings import MEDIA_ROOT
from user.views import *

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    re_path('media/(?P<path>.*)', serve, {"document_root": MEDIA_ROOT}),
    path('ueditor/', include('DjangoUeditor.urls')),
    path("user/", include('user.urls', namespace="user")),
    path('', include('goods.urls', namespace='goods')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('order/', include('order.urls', namespace='order')),
]
