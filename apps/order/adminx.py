
import xadmin
from .models import OrderDetailInfo, OrderInfo


class OrderInfoAdmin(object):

    list_display = ["oid", "user", "odate", "ototal", "oaddress"]
    list_per_page = 5
    list_filter = ["user", "odate", "oaddress"]
    search_fields = ["user__uname"]
    ordering = ["-odate"]



class OrderDetailInfoAdmin(object):

    list_display = ["goods", "order", "price", "count"]
    list_per_page = 5
    list_filter = ["goods"]


xadmin.site.register(OrderInfo, OrderInfoAdmin)
xadmin.site.register(OrderDetailInfo, OrderDetailInfoAdmin)
