"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from .views import *
urlpatterns = [

    url(r'^$',index),

    url(r'^base/$',base),

    url(r'^all_products/$',all_products),

    url(r'^products_types/(\d+)/$',products_types),

    url(r'^search/$',search),

    url(r'^register/$',register),#注册

    url(r'^login/$',login),#登录

    url(r'^quit/$',quit),#登录

    url(r'^detailpage/(\d+)/$',detailpage),#详情页

    url(r'^pay/$',pay),#

    url(r'^ok/$',ok),#

    url(r'^wuliu/(\d+)/$',wuliu),#


    # 个人中心主页
    url(r'^personal_index/$',personal_index),

    url(r'^personal_account/$',personal_account),#账户安全

    url(r'^personal_info/$',personal_info),#账户安全

    url(r'^personal_login_pass/$',personal_login_pass),#联系人

    url(r'^personal_resetPay/$',personal_resetPay),#重置密码

    url(r'^personal_address/$',personal_address),#地址

    url(r'^personal_comment/$', personal_comment),  # 我的评价
    url(r'^chakanpinglun$', chakanpinglun),  # 我的评价

    url(r'^personal_order/$', personal_order),  # 我的订单
    url(r'^place_an_order$',place_an_order),#
    url(r'^querenshouhuo$',querenshouhuo),#确认收货

    url(r'^delete_order$',delete_order),#删除订单

    url(r'^personal_shopcar/$', personal_shopcar),  # 登录 $非贪婪查询  确保精准查询
    url(r'^join_gouwuche$', join_gouwuche),  # 加入购物车
    url(r'^quxiao_gouwuche$', quxiao_gouwuche),  # 取消购物车

    url(r'^personal_shoucang/$', personal_shoucang),#我的收藏
    url(r'^jiashoucang$', jiashoucang),#商品加入收藏

    url(r'^personal_post/$', personal_post),#发布商品

]
