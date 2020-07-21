from django.contrib import admin
from .models import *
#这是是注册，注册了之后才能在django后台显示

@admin.register(Login)
class Postlogin(admin.ModelAdmin):
    list_display = ('username','nickname','created_time','modified_time')#在 处展示
    search_fields = ['username']  # 添加搜索字段 按类别 category__categoty_name
    list_per_page = 10  # 一页三条数据

@admin.register(Favorite)
class Favorite(admin.ModelAdmin):
    list_display = ('user','goods','created_time')#在 处展示
    list_per_page = 10  # 一页三条数据

@admin.register(Product_Types)
class Product_Types(admin.ModelAdmin):
    list_display = ('name',)#在 处展示
    list_per_page = 10  # 一页三条数据

@admin.register(Adress)
class Adress(admin.ModelAdmin):
    list_display = ('user','ads','phone')#在 处展示
    list_per_page = 10  # 一页三条数据

@admin.register(Order)
class Order(admin.ModelAdmin):
    list_display = ('user','orderNo','orderstatus','adress','acot','acount')#在 处展示
    list_per_page = 10  # 一页三条数据

@admin.register(CartInfo)
class Carinfo(admin.ModelAdmin):
    list_display = ('user','goods','store','ccount')#在 处展示
    list_per_page = 10  # 一页三条数据

@admin.register(Token)
class Token(admin.ModelAdmin):
    list_display = ('user', 'token')  # 在 处展示
    list_per_page = 10  # 一页三条数据

@admin.register(Comment)
class c(admin.ModelAdmin):
    list_display = ['username','content','goods','time']

@admin.register(Balance)
class c(admin.ModelAdmin):
    list_display = ['user','amount','time']

class Good(admin.ModelAdmin):
    list_display = ['user','title','price','unit',
                    'type','sales','look','Seven_days_package_Return','Free_shipping']
    fieldsets = (
         ('卖家', {'fields': ['user']}),

         ('商品价格', {'fields': ['price']}),


         ('商品名称/简单描述/商品详情',{'fields':['title','desc','content']}),#author 是昵称，author_账号

         ('商品分类',{'fields':['type']}),

         ('商品主图片/副图片',{'fields':['picture','picture1','picture2','picture3','picture4']}),

         ('商品颜色分类',{'fields':['picture_color1','picture_color2','picture_color3','picture_color4']}),

         ('商品单位', {'fields': ['unit']}),

         ('库存', {'fields': ['quantity']}),

         ('是否七天包退换',{'fields':['Seven_days_package_Return']}),

         ('是否包邮',{'fields':['Free_shipping']}),

         ('邮费',{'fields':['postage']}),


    )

    list_filter = ['title']
    list_per_page = 15

class p_line(admin.TabularInline):
    model = Goods
    extra = 15
admin.site.register(Goods,Good)


