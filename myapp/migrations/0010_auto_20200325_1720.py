# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_auto_20200325_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='acot',
            field=models.IntegerField(verbose_name='总数', blank=True, default=1),
        ),
        migrations.AlterField(
            model_name='order',
            name='orderNo',
            field=models.CharField(verbose_name='订单编号', max_length=50),
        ),
    ]
