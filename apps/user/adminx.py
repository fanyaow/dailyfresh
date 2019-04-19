from django.contrib import admin

# Register your models here.
import xadmin
from order.models import OrderInfo, OrderDetailInfo
from cart.models import CartInfo
from .models import UserInfo, GoodsBrowser, Banner, Advert
from xadmin import views
from goods.models import GoodsInfo, TypeInfo


# X admin的全局配置信息设置
class BaseSetting(object):
    # 主题功能开启
    enable_themes = True
    use_bootswatch = True


# x admin 全局配置参数信息设置
class GlobalSettings(object):
    site_title = " 天天生鲜后台管理站"
    site_footer = "天天生鲜后台管理站"

    # 收起菜单
    menu_style = "accordion"

    def get_site_menu(self):
        return (
            {'title': '用户管理', 'menus': (
                {'title': '用户信息', 'url': self.get_model_url(UserInfo, 'changelist')},
                {'title': '用户浏览记录', 'url': self.get_model_url(GoodsBrowser, 'changelist')},
                {'title': '轮播图管理', 'url': self.get_model_url(Banner, 'changelist')},
                {'title': '侧边广告管理', 'url': self.get_model_url(Advert, 'changelist')},
            )},
            {'title': '商品管理', 'menus': (
                {'title': '商品信息', 'url': self.get_model_url(GoodsInfo, 'changelist')},
                {'title': '商品类别', 'url': self.get_model_url(TypeInfo, 'changelist')},
            )},
            {'title': '订单管理', 'menus': (
                {'title': '订单列表', 'url': self.get_model_url(OrderInfo, 'changelist')},
                {'title': '订单明细', 'url': self.get_model_url(OrderDetailInfo, 'changelist')},
            )},
            {'title': '购物车', 'menus': (
                {'title': '购物车', 'url': self.get_model_url(CartInfo, 'changelist')},
            )},
        )


class UserInfoAdmin(object):
    list_display = ["uname", "uemail", "ushou", "uaddress", "uyoubian", "uphone", 'image_img']
    list_per_page = 5
    list_filter = ["uname", "uyoubian"]
    search_fields = ["uname", "uyoubian"]
    readonly_fields = ["uname"]


class GoodsBrowserAdmin(object):
    list_display = ["user", "good"]
    list_per_page = 50
    list_filter = ["user__uname", "good__gtitle"]
    search_fields = ["user__uname", "good__gtitle"]
    readonly_fields = ["user", "good"]
    refresh_times = [3, 5]


class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    search_fields = ['title', 'image', 'url', 'index']
    list_filter = ['title', 'image', 'url', 'index', 'add_time']
    list_display_links = ['title']


class AdvertAdmin(object):
    list_display = ['id','adname','adtype', 'adimage', 'adurl', 'adindex', 'ad_time']
    search_fields = ['adname',  'url', 'index']
    list_filter = ['adname',  'ad_time']
    list_display_links = ['adname']


xadmin.site.register(UserInfo, UserInfoAdmin)
xadmin.site.register(GoodsBrowser, GoodsBrowserAdmin)
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(Advert, AdvertAdmin)
# 将Xadmin全局管理器与我们的view绑定注册。
xadmin.site.register(views.BaseAdminView, BaseSetting)

# 将头部与脚部信息进行注册:
xadmin.site.register(views.CommAdminView, GlobalSettings)
