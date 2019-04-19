from django.conf.urls import url
from django.urls import path, re_path

from goods.views import banner
from . import views

app_name = 'goods'

urlpatterns = [
    path('', views.index, name="index"),
    re_path(r'^list(\d+)_(\d+)_(\d+)/$', views.good_list, name="good_list"),
    re_path(r'^(\d+)/$', views.detail, name="detail"),
    path('search/', views.ordinary_search, name="ordinary_search"),  # 全文检索
    path('banner/', banner, name='banner')
]
