from django.db import models
from .models import *
from DjangoUeditor.models import UEditorField
from django.contrib.auth.models import User
import os
from web import settings
from PIL import Image
from django.db.models.fields.files import ImageFieldFile
import time
#这里是MVT中的 M，用于把你写的代码进行相应数据库的转化
#每次更新了新的字段（列），就要运行
# python manage.py makemigrations 迁移
# python manage.py migrate 生效


#逻辑删除
class MyloginManager(models.Manager): #逻辑删除 重写类 可以在后台中屏蔽 被逻辑删除的对象
    def get_queryset(self):
        # super(PostManage,self).get_queryset() #调用父类的方法
        #  只返回没有被逻辑删除的文章
        return super(MyloginManager,self).get_queryset().filter(is_delete=0)


#用户表
class Login(models.Model):

    nickname = models.CharField('昵称', max_length=32,blank=True,default="无名")

    avatar = models.ImageField("头像",blank=True)  # 图片

    username = models.CharField('用户名',unique=True, max_length=32)  #

    password = models.CharField('密码', max_length=250)  #

    birthday = models.CharField('生日', max_length=32,blank=True)  #生日

    sex = models.CharField('性别',max_length=32,blank=True,default="男")  #性别

    city = models.CharField('所在城市',max_length=32,blank=True)  #城市

    email = models.EmailField('邮箱',blank=True)  #邮箱

    phone = models.CharField('手机号', max_length=32,blank=True)  #手机号

    # 建立时间 不能修改
    created_time=models.DateTimeField('建立时间',auto_now_add=True)

    # 修改时间 每次自动更新
    modified_time=models.DateTimeField('修改时间',auto_now=True)


    is_delete=models.BooleanField(default=False,verbose_name='逻辑删除',help_text='逻辑删除')

    def delete(self, using=None,keep_parents=False):
        #重写数据库删除方法 实现逻辑删除
        self.is_delete=True
        self.save()

    class Meta:
        verbose_name_plural = '注册用户'
        ordering = ["-modified_time"]

    def __str__(self):
        return self.nickname

    objects = MyloginManager()#逻辑删除 在后台过滤 被逻辑删除的用户

# 商品类型
class Product_Types(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "商品类型"


#商品
class Goods(models.Model):
    user = models.ForeignKey(Login)

    title = models.CharField('商品名称', max_length=30, null=False)
    price = models.DecimalField('商品价格', max_digits=8, decimal_places=2)
    desc = models.CharField('描述', max_length=200)

    content = UEditorField('商品详情', width=800, height=600, imagePath="myapp/")

    unit = models.CharField('单位', max_length=30)
    picture = models.ImageField('商品图片')

    picture1 = models.ImageField('商品详情图片1',blank=True)
    picture2 = models.ImageField('商品详情图片2',blank=True)
    picture3 = models.ImageField('商品详情图片3',blank=True)
    picture4 = models.ImageField('商品详情图片4',blank=True)


    picture_color1 = models.ImageField('商品颜色1',blank=True)
    picture_color2 = models.ImageField('商品颜色2',blank=True)
    picture_color3 = models.ImageField('商品颜色3',blank=True)
    picture_color4 = models.ImageField('商品颜色4',blank=True)


    type = models.ForeignKey(Product_Types)

    Seven_days_package_Return=models.BooleanField(default=True,verbose_name='七天包退换',help_text='七天包退换')

    Free_shipping=models.BooleanField(default=True,verbose_name='包邮',help_text='包邮')

    postage=models.IntegerField("邮费",blank=True,default=0)

    quantity=models.IntegerField("库存",default=1)

    sales=models.IntegerField("销量", default=0)
    look = models.IntegerField('浏览量', default=0)



    # 建立时间 不能修改
    created_time=models.DateTimeField('建立时间',auto_now_add=True)

    # 修改时间 每次自动更新
    modified_time=models.DateTimeField('修改时间',auto_now=True)

    def increase_look(self):
        self.look += 1
        self.save(update_fields=['look'])

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "商品"


#Token表用于登录认证
class Token(models.Model):
    user = models.OneToOneField(to=Login, on_delete=models.CASCADE)
    token = models.CharField('token', max_length=255)

    def __str__(self):
        return self.token
    class Meta:
        verbose_name_plural="认证"


#购物车
class CartInfo(models.Model):
    user = models.ForeignKey(Login,related_name='user')
    store = models.ForeignKey(Login,related_name='store')#店铺名

    goods = models.ForeignKey(Goods)
    ccount = models.IntegerField('数量')
    created_time = models.DateTimeField('加入购物车时间',auto_now_add=True)

    def __unicode__(self):
        return "%s likes picture %s" % (self.user, self.goods)

    class Meta:
        verbose_name_plural="购物车"

#用户收藏夹
class Favorite(models.Model):

    user = models.ForeignKey(Login)
    goods = models.ForeignKey(Goods)
    created_time = models.DateTimeField('收藏时间',auto_now_add=True)

    def __unicode__(self):
        return "%s likes picture %s" % (self.user, self.picture)

    class Meta:
        verbose_name_plural="收藏"


#收货地址
class Adress(models.Model):
    user = models.ForeignKey(Login, on_delete=models.CASCADE)
    receiver_name=models.CharField("收件人姓名",max_length=24)
    area=models.CharField("地区",max_length=24)
    postcode=models.IntegerField("邮编")
    ads = models.CharField('详细地址', max_length=300, null=False)
    phone = models.CharField('电话', max_length=20, null=False)

    def __str__(self):
        return self.ads

    class Meta:
        verbose_name_plural="收货地址"


#订单
class Order(models.Model):
    user = models.ForeignKey(Login)
    goods = models.ForeignKey(Goods)

    ORDERSTATUS = (
        ('未支付', '未支付',),
        ('已支付', '已支付',),
        ('订单取消', '订单取消',),
        ('已收货', '已收货',),
    )
    orderNo = models.CharField('订单编号', max_length=50)

    adress=models.ForeignKey(Adress)

    time = models.DateTimeField(auto_now=True)
    acot = models.IntegerField('总数',blank=True,default=1)
    acount = models.DecimalField('总价', max_digits=8, decimal_places=2)

    orderstatus = models.CharField('订单状态',max_length=32, choices=ORDERSTATUS, default="未支付")

    is_comment=models.BooleanField('是否评价',default=False)


    def __str__(self):
        return self.orderNo

    class Meta:
        verbose_name_plural="订单"


#评论表
class Comment(models.Model):
    choices = (
        ('五星好评', '五星好评',),
        ('四星好评', '四星好评',),
        ('三星中评', '三星中评',),
        ('二星差评', '二星差评',),
        ('一星差评', '一星差评',),
    )
    type = models.CharField('评价类型',max_length=32, choices=choices, default="五星好评")

    username=models.ForeignKey(Login)



    content= UEditorField('评价内容', width=800, height=600, imagePath="myapp/")

    time=models.DateTimeField(auto_now_add=True)

    #关联商品
    goods=models.ForeignKey(Goods)

    order=models.ForeignKey(Order)

    is_comment=models.BooleanField('是否评价',default=False)

    def post_id(self):
        return self.post
    post_id.short_description="文章"

    class Meta:
        verbose_name_plural="评论"
        # ordering = ["-time"]  # 按降序排列

#账户余额
class Balance(models.Model):

    user=models.ForeignKey(Login)

    amount = models.DecimalField('金额',default=1000, max_digits=12, decimal_places=2 )

    def add_amount(self,num):
        self.amount += num
        self.save(update_fields=['amount'])

    def Less_amount(self,num):
        self.amount -= num

        self.save(update_fields=['amount'])

    time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name_plural = "账户余额"


