# Create your models here.
from django.db import models
# 将一对多的关系维护在GoodsInfo中维护，另外商品信息与分类信息都属于重要信息需要使用逻辑删除
from DjangoUeditor.models import UEditorField
from stdimage.models import StdImageField


class TypeInfo(models.Model):
    # 商品分类信息  水果 海鲜等
    isDelete = models.BooleanField(default=False)

    tpic = StdImageField(
        default='goods/default.jpg',
        upload_to="goods/%Y/%m",
        verbose_name=u"分类图标",
        variations={'thumbnail': {'width': 100, 'height': 75}},
        max_length=100)
    ttitle = models.CharField(max_length=20, verbose_name="分类")

    class Meta:
        verbose_name = "商品类型"
        verbose_name_plural = verbose_name

    def url(self):
        if self.tpic:
            return self.tpic.url
        else:
            return "url为空"

    def timage_img(self):
        if self.tpic:
            href = self.tpic.url  # 点击后显示的放大图片
            src = self.tpic.thumbnail.url  # 页面显示的缩略图
            # 插入html代码
            image_html = '<a href="%s" target="_blank" title="传图片"><img alt="" src="%s"/>' % (href, src)
            return image_html
        else:
            return '上传图片'

    timage_img.short_description = '图片'
    timage_img.allow_tags = True  # 列表页显示图片

    def __str__(self):
        return self.ttitle


class GoodsInfo(models.Model):
    # 具体商品信息
    isDelete = models.BooleanField(default=False)  # 逻辑删除
    gtitle = models.CharField(max_length=20, verbose_name="商品名称", unique=True)
    gpic = StdImageField(
        default='goods/default.jpg',
        upload_to="goods/%Y/%m",
        verbose_name=u"商品图片",
        variations={'thumbnail': {'width': 100, 'height': 75}},
        max_length=100)
    gprice = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="商品价格",
                                 max_length=20)  # 商品价格小数位为两位，整数位为3位
    gunit = models.CharField(max_length=20, default='500g', verbose_name="单位重量")
    gclick = models.IntegerField(verbose_name="点击量", blank=False, default=1)
    gjianjie = models.CharField(max_length=200, verbose_name="简介")
    gkucun = models.IntegerField(verbose_name="库存")
    gcontent = UEditorField(verbose_name=u"商品详情", width=600, height=300, imagePath="goods/ueditor/",
                            filePath="goods/ueditor/", default='')
    gtype = models.ForeignKey(TypeInfo, on_delete=models.CASCADE, verbose_name="分类")  # 外键关联TypeInfo表

    # gadv = models.BooleanField(default=False) #商品是否推荐

    class Meta:
        verbose_name = "商品"
        verbose_name_plural = verbose_name

    def url(self):
        if self.gpic:
            return self.gpic.url
        else:
            return "url为空"

    def image_img(self):
        if self.gpic:
            href = self.gpic.url  # 点击后显示的放大图片
            src = self.gpic.thumbnail.url  # 页面显示的缩略图
            # 插入html代码
            image_html = '<a href="%s" target="_blank" title="传图片"><img alt="" src="%s"/>' % (href, src)
            return image_html
        else:
            return '上传图片'

    image_img.short_description = '图片'
    image_img.allow_tags = True  # 列表页显示图片

    def __str__(self):
        return self.gtitle
