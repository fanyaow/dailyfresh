import xadmin

from .models import TypeInfo, GoodsInfo


# Register your models here.

class TypeInfoAdmin(object):
    list_display = ['id', 'ttitle', 'timage_img']
    list_per_page = 10
    search_fields = ['ttitle']
    list_display_links = ['ttitle']


class GoodsInfoAdmin(object):
    list_per_page = 20
    style_fields = {'gcontent': "ueditor"}
    list_display = ['id', 'gtitle', 'gunit', 'gclick', 'gprice', 'image_img', 'gkucun', 'gjianjie']
    list_editable = ['gkucun', 'gjianjie', 'gclick', 'gprice']
    search_fields = ['gtitle', 'gjianjie']
    list_display_links = ['gtitle']


xadmin.site.register(TypeInfo, TypeInfoAdmin)
xadmin.site.register(GoodsInfo, GoodsInfoAdmin)
