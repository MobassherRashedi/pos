# Generated by Django 4.1.4 on 2022-12-26 05:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0011_alter_sendemail_created_at_alter_sendsms_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sendemail',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 26, 11, 21, 33, 309168)),
        ),
        migrations.AlterField(
            model_name='sendsms',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 26, 11, 21, 33, 309168)),
        ),
    ]
