# Generated by Django 4.1.4 on 2022-12-21 10:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0009_alter_catagory_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catagory',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 21, 16, 24, 25, 198994)),
        ),
        migrations.AlterField(
            model_name='companyinfo',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 21, 16, 24, 25, 198994)),
        ),
        migrations.AlterField(
            model_name='customer',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 21, 16, 24, 25, 198994)),
        ),
        migrations.AlterField(
            model_name='customer',
            name='customer_code',
            field=models.CharField(default='C3348927', max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='subcatagory',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 21, 16, 24, 25, 198994)),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 21, 16, 24, 25, 198994)),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='supplier_code',
            field=models.CharField(default='S3685971', max_length=10, unique=True),
        ),
    ]