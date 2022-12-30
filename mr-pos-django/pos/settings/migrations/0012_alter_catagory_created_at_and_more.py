# Generated by Django 4.1.4 on 2022-12-26 05:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0011_alter_catagory_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catagory',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 26, 11, 6, 2, 368440)),
        ),
        migrations.AlterField(
            model_name='companyinfo',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 26, 11, 6, 2, 368440)),
        ),
        migrations.AlterField(
            model_name='customer',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 26, 11, 6, 2, 368440)),
        ),
        migrations.AlterField(
            model_name='customer',
            name='customer_code',
            field=models.CharField(default='C5746362', max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='subcatagory',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 26, 11, 6, 2, 368440)),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 26, 11, 6, 2, 368440)),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='supplier_code',
            field=models.CharField(default='S6835891', max_length=10, unique=True),
        ),
    ]
