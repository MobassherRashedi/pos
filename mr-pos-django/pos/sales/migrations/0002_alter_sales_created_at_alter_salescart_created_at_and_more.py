# Generated by Django 4.1.4 on 2022-12-14 11:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sales',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 14, 17, 45, 10, 29955)),
        ),
        migrations.AlterField(
            model_name='salescart',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 14, 17, 45, 10, 29955)),
        ),
        migrations.AlterField(
            model_name='salescartamount',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 14, 17, 45, 10, 29955)),
        ),
    ]
