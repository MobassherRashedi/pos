# Generated by Django 4.1.4 on 2022-12-30 14:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0014_alter_sendemail_created_at_alter_sendsms_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sendemail',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 30, 20, 56, 52, 513161)),
        ),
        migrations.AlterField(
            model_name='sendsms',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 30, 20, 56, 52, 513161)),
        ),
    ]
