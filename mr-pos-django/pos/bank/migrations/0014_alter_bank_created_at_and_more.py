# Generated by Django 4.1.4 on 2022-12-26 05:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0013_alter_bank_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bank',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 26, 11, 21, 33, 309168)),
        ),
        migrations.AlterField(
            model_name='banktransaction',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 26, 11, 21, 33, 309168)),
        ),
        migrations.AlterField(
            model_name='banktransactiontype',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 26, 11, 21, 33, 309168)),
        ),
    ]