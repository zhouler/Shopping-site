# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0016_auto_20200329_1128'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='picture1',
            field=models.ImageField(verbose_name='商品详情图片', blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='goods',
            name='picture2',
            field=models.ImageField(verbose_name='商品详情图片', blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='goods',
            name='picture3',
            field=models.ImageField(verbose_name='商品详情图片', blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='goods',
            name='picture4',
            field=models.ImageField(verbose_name='商品详情图片', blank=True, upload_to=''),
        ),
    ]
