# Generated by Django 4.1.4 on 2022-12-19 05:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0005_alter_asset_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 19, 11, 2, 28, 682796)),
        ),
    ]
