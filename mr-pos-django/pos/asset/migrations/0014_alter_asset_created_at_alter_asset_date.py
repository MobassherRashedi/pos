# Generated by Django 4.1.4 on 2022-12-29 18:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0013_alter_asset_created_at_alter_asset_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 30, 0, 16, 43, 772983)),
        ),
        migrations.AlterField(
            model_name='asset',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 12, 29, 18, 16, 43, 814960, tzinfo=datetime.timezone.utc), null=True),
        ),
    ]
