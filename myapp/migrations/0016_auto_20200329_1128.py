# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_auto_20200327_1546'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='created_time',
            field=models.DateTimeField(verbose_name='建立时间', default=datetime.datetime(2020, 3, 29, 11, 28, 30, 495010), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='goods',
            name='modified_time',
            field=models.DateTimeField(verbose_name='修改时间', default=datetime.datetime(2020, 3, 29, 11, 28, 35, 203010), auto_now=True),
            preserve_default=False,
        ),
    ]
