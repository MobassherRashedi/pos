# Generated by Django 4.1.4 on 2022-12-30 20:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0015_alter_sendemail_created_at_alter_sendsms_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sendemail',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 31, 2, 12, 46, 91824)),
        ),
        migrations.AlterField(
            model_name='sendsms',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 31, 2, 12, 46, 91824)),
        ),
    ]
