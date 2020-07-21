# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0020_comment_is_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='goods',
            field=models.ForeignKey(default=1, to='myapp.Goods'),
            preserve_default=False,
        ),
    ]
