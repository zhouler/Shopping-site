# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0026_auto_20200408_1852'),
    ]

    operations = [
        migrations.AddField(
            model_name='login',
            name='phone',
            field=models.CharField(verbose_name='手机号', max_length=32, blank=True),
        ),
    ]
