# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20200304_1050'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='orderdetail',
        ),
        migrations.AddField(
            model_name='comment',
            name='orderstatus',
            field=models.IntegerField(verbose_name='订单', default=1, choices=[(1, '五星好评'), (1, '四星好评'), (3, '三星中评'), (4, '二星差评'), (5, '一星垃圾')]),
        ),
    ]
