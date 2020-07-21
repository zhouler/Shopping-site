# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0027_login_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product_Types',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': '商品类型',
            },
        ),
        migrations.AlterField(
            model_name='goods',
            name='type',
            field=models.ForeignKey(to='myapp.Product_Types'),
        ),
    ]
