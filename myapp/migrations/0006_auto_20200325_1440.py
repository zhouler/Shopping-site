# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import DjangoUeditor.models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_goods_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=DjangoUeditor.models.UEditorField(verbose_name='评价内容'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='quantity',
            field=models.IntegerField(verbose_name='库存', default=1),
        ),
    ]
