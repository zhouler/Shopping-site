# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0017_auto_20200330_1718'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='picture_color1',
            field=models.ImageField(verbose_name='商品颜色1', blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='goods',
            name='picture_color2',
            field=models.ImageField(verbose_name='商品颜色2', blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='goods',
            name='picture_color3',
            field=models.ImageField(verbose_name='商品颜色3', blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='goods',
            name='picture_color4',
            field=models.ImageField(verbose_name='商品颜色4', blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='goods',
            name='picture1',
            field=models.ImageField(verbose_name='商品详情图片1', blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='goods',
            name='picture2',
            field=models.ImageField(verbose_name='商品详情图片2', blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='goods',
            name='picture3',
            field=models.ImageField(verbose_name='商品详情图片3', blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='goods',
            name='picture4',
            field=models.ImageField(verbose_name='商品详情图片4', blank=True, upload_to=''),
        ),
    ]
