# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0018_auto_20200330_1728'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='is_comment',
            field=models.BooleanField(verbose_name='是否评价', default=False),
        ),
    ]
