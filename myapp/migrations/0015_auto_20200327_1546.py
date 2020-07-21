# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_cartinfo_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='adress',
            name='area',
            field=models.CharField(verbose_name='地区', max_length=24, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='adress',
            name='postcode',
            field=models.IntegerField(verbose_name='邮编', default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='adress',
            name='receiver_name',
            field=models.CharField(verbose_name='收件人姓名', max_length=24, default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='adress',
            name='ads',
            field=models.CharField(verbose_name='详细地址', max_length=300),
        ),
    ]
