# Generated by Django 4.1.4 on 2022-12-20 10:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0006_rename_returened_sales_returned_sales_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sales',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 20, 16, 43, 56, 539266)),
        ),
        migrations.AlterField(
            model_name='sales',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 12, 20, 16, 43, 56, 570515), null=True, verbose_name='date'),
        ),
        migrations.AlterField(
            model_name='salescart',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 20, 16, 43, 56, 539266)),
        ),
        migrations.AlterField(
            model_name='salescartamount',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 20, 16, 43, 56, 539266)),
        ),
    ]
