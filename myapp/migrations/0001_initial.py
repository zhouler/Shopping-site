# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import DjangoUeditor.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adress',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('ads', models.CharField(verbose_name='地址', max_length=300)),
                ('phone', models.CharField(verbose_name='电话', max_length=20)),
            ],
            options={
                'verbose_name_plural': '收货地址',
            },
        ),
        migrations.CreateModel(
            name='CartInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('ccount', models.IntegerField(verbose_name='数量')),
                ('created_time', models.DateTimeField(verbose_name='加入购物车时间', auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': '购物车',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('content', models.TextField(max_length=1000)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': '评论',
            },
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('created_time', models.DateTimeField(verbose_name='收藏时间', auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': '收藏',
            },
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(verbose_name='商品名称', max_length=30)),
                ('price', models.DecimalField(verbose_name='商品价格', max_digits=8, decimal_places=2)),
                ('desc', models.CharField(verbose_name='描述', max_length=200)),
                ('content', DjangoUeditor.models.UEditorField(verbose_name='商品详情')),
                ('unit', models.CharField(verbose_name='单位', max_length=30)),
                ('picture', models.ImageField(verbose_name='商品图片', upload_to='')),
                ('type', models.CharField(verbose_name='分类名称', max_length=30)),
                ('sales', models.IntegerField(verbose_name='销量', default=0)),
                ('look', models.IntegerField(verbose_name='浏览量', default=0)),
            ],
            options={
                'verbose_name_plural': '商品',
            },
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('nickname', models.CharField(verbose_name='昵称', max_length=32, blank=True, default='无名')),
                ('avatar', models.ImageField(verbose_name='头像', blank=True, upload_to='')),
                ('username', models.CharField(verbose_name='用户名', max_length=32, unique=True)),
                ('password', models.CharField(verbose_name='密码', max_length=250)),
                ('birthday', models.CharField(verbose_name='生日', max_length=32, blank=True)),
                ('sex', models.CharField(verbose_name='性别', max_length=32, blank=True, default='男')),
                ('city', models.CharField(verbose_name='所在城市', max_length=32, blank=True)),
                ('email', models.EmailField(verbose_name='邮箱', max_length=254, blank=True)),
                ('created_time', models.DateTimeField(verbose_name='建立时间', auto_now_add=True)),
                ('modified_time', models.DateTimeField(verbose_name='修改时间', auto_now=True)),
                ('is_delete', models.BooleanField(verbose_name='逻辑删除', default=False, help_text='逻辑删除')),
            ],
            options={
                'verbose_name_plural': '注册用户',
                'ordering': ['-modified_time'],
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('orderNo', models.CharField(verbose_name='商品编号', max_length=50)),
                ('orderdetail', models.TextField(verbose_name='订单详情')),
                ('time', models.DateTimeField(auto_now=True)),
                ('acot', models.IntegerField(verbose_name='总数')),
                ('acount', models.DecimalField(verbose_name='总价', max_digits=8, decimal_places=2)),
                ('orderstatus', models.IntegerField(verbose_name='订单', default=1, choices=[(1, '未支付'), (2, '已支付'), (3, '订单取消')])),
                ('adress', models.ForeignKey(to='myapp.Adress')),
                ('user', models.ForeignKey(to='myapp.Login')),
            ],
            options={
                'verbose_name_plural': '订单',
            },
        ),
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('token', models.CharField(verbose_name='token', max_length=255)),
                ('user', models.OneToOneField(to='myapp.Login')),
            ],
            options={
                'verbose_name_plural': '认证',
            },
        ),
        migrations.AddField(
            model_name='goods',
            name='user',
            field=models.ForeignKey(to='myapp.Login'),
        ),
        migrations.AddField(
            model_name='favorite',
            name='goods',
            field=models.ForeignKey(to='myapp.Goods'),
        ),
        migrations.AddField(
            model_name='favorite',
            name='user',
            field=models.ForeignKey(to='myapp.Login'),
        ),
        migrations.AddField(
            model_name='comment',
            name='goods',
            field=models.ForeignKey(to='myapp.Goods'),
        ),
        migrations.AddField(
            model_name='comment',
            name='username',
            field=models.ForeignKey(to='myapp.Login'),
        ),
        migrations.AddField(
            model_name='cartinfo',
            name='good',
            field=models.ForeignKey(to='myapp.Goods'),
        ),
        migrations.AddField(
            model_name='cartinfo',
            name='user',
            field=models.ForeignKey(to='myapp.Login'),
        ),
        migrations.AddField(
            model_name='adress',
            name='user',
            field=models.ForeignKey(to='myapp.Login'),
        ),
    ]
