# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_auto_20200327_1059'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartinfo',
            name='pic',
            field=models.ImageField(verbose_name='商品图片', blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='cartinfo',
            name='title',
            field=models.CharField(verbose_name='标题', max_length=64, blank=True, default='标题'),
        ),
    ]
