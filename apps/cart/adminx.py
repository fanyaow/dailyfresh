from django.contrib import admin
import xadmin
from .models import CartInfo


# Register your models here.
class CartInfoAdmin(object):
    list_display = ['user', 'goods', 'count']
    list_per_page = 5
    list_filter = ['user', 'goods', 'count']
    search_fields = ['user_uname', 'goods__gtitle']
    readonly_fields = ['user', 'goods', 'count']


xadmin.site.register(CartInfo, CartInfoAdmin)
