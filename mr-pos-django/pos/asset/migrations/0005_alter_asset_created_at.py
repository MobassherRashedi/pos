# Generated by Django 4.1.4 on 2022-12-17 10:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0004_alter_asset_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 17, 16, 36, 34, 140289)),
        ),
    ]