# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-08-01 04:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20170801_1045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_details',
            name='color_img',
            field=models.ImageField(blank=True, null=True, upload_to=b'shop/product/%Y/%m'),
        ),
        migrations.AlterField(
            model_name='product_details',
            name='small_img',
            field=models.ImageField(blank=True, null=True, upload_to=b'shop/product/%Y/%m'),
        ),
    ]
