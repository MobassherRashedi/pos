# Generated by Django 4.1.4 on 2022-12-30 06:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0013_alter_product_created_at_alter_product_product_code_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='in_stock',
            field=models.BooleanField(default=True, verbose_name='In Stock'),
        ),
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 30, 12, 20, 19, 222220)),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_code',
            field=models.CharField(default='P3143629', max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='productimages',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 30, 12, 20, 19, 222220)),
        ),
        migrations.AlterField(
            model_name='productunittype',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 30, 12, 20, 19, 222220)),
        ),
    ]
