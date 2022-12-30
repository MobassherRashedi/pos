# Generated by Django 4.1.4 on 2022-12-21 10:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_rename_returened_product_returned_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 21, 16, 3, 25, 305883)),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_code',
            field=models.CharField(default='P1297732', max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='productimages',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 21, 16, 3, 25, 305883)),
        ),
        migrations.AlterField(
            model_name='productunittype',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 21, 16, 3, 25, 305883)),
        ),
    ]
