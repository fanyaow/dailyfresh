from django.db import models

from datetime import datetime

from goods.models import GoodsInfo,TypeInfo
from stdimage.models import StdImageField


class UserInfo(models.Model):
    uname = models.CharField(max_length=20, verbose_name="用户名", unique=True)
    upwd = models.CharField(max_length=40, verbose_name="用户密码", blank=False)
    uemail = models.EmailField(verbose_name="邮箱", unique=True)
    avatar = StdImageField(
        default='image/default.jpg',
        upload_to="image/%Y/%m",
        verbose_name=u"我的头像",
        variations={'thumbnail': {'width': 100, 'height': 75}},
        max_length=100)
    ushou = models.CharField(max_length=20, default="", verbose_name="收货地址")
    uaddress = models.CharField(max_length=100, default="", verbose_name="地址")
    uyoubian = models.CharField(max_length=6, default="", verbose_name="邮编")
    uphone = models.CharField(max_length=11, default="", verbose_name="手机号")

    # default,blank是python层面的约束，不影响数据库表结构，修改时不需要迁移 python manage.py makemigrations

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def url(self):
        if self.avatar:
            return self.avatar.url
        else:
            return "url为空"

    def image_img(self):
        if self.avatar:
            href = self.avatar.url  # 点击后显示的放大图片
            src = self.avatar.thumbnail.url  # 页面显示的缩略图
            # 插入html代码
            image_html = '<a href="%s" target="_blank" title="传图片"><img alt="" src="%s"/>' % (href, src)
            return image_html
        else:
            return '上传图片'

    image_img.short_description = '头像图片'
    image_img.allow_tags = True  # 列表页显示图片

    def __str__(self):
        return self.uname


class GoodsBrowser(models.Model):
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE, verbose_name="用户ID")
    good = models.ForeignKey(GoodsInfo, on_delete=models.CASCADE, verbose_name="商品ID")
    browser_time = models.DateTimeField(default=datetime.now, verbose_name="浏览时间")

    class Meta:
        verbose_name = "用户浏览记录"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{0}浏览记录{1}".format(self.user.uname, self.good.gtitle)


# 轮播图
class Banner(models.Model):
    title = models.CharField(max_length=100, verbose_name=u"标题")
    image = models.ImageField(
        upload_to="banner/%Y/%m",
        verbose_name=u"轮播图",
        max_length=100)
    url = models.URLField(max_length=200, verbose_name=u"访问地址")
    # 默认index很大靠后。想要靠前修改index值。
    index = models.IntegerField(default=100, verbose_name=u"顺序")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"轮播图"
        verbose_name_plural = verbose_name

    # 重载__str__方法使后台不再直接显示object
    def __str__(self):
        return '{0}(位于第{1}位)'.format(self.title, self.index)


class Advert(models.Model):
    adname = models.CharField(max_length=50,verbose_name='广告名称')
    adtype = models.ForeignKey(TypeInfo, on_delete=models.CASCADE, verbose_name='广告类别')
    adimage = models.ImageField(
        upload_to="advert/%Y/%m",
        verbose_name=u"侧边广告图",
        max_length=100)
    adurl = models.URLField(max_length=200, verbose_name=u"访问地址")
    # 默认index很大靠后。想要靠前修改index值。
    adindex = models.IntegerField(default=100, verbose_name=u"顺序")
    ad_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"侧边广告"
        verbose_name_plural = verbose_name

    # 重载__str__方法使后台不再直接显示object
    def __str__(self):
        return '{0}(位于第{1}位)'.format(self.adname, self.adindex)