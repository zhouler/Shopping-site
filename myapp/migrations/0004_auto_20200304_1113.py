# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20200304_1104'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='Free_shipping',
            field=models.BooleanField(verbose_name='包邮', default=True, help_text='包邮'),
        ),
        migrations.AddField(
            model_name='goods',
            name='Seven_days_package_Return',
            field=models.BooleanField(verbose_name='七天包退换', default=True, help_text='七天包退换'),
        ),
        migrations.AddField(
            model_name='goods',
            name='postage',
            field=models.IntegerField(verbose_name='邮费', blank=True, default=0),
        ),
    ]
