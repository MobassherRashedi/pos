# Generated by Django 4.1.4 on 2022-12-29 18:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('damages', '0012_alter_damages_created_at_alter_damages_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='damages',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 30, 0, 16, 43, 772983)),
        ),
        migrations.AlterField(
            model_name='damages',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 30, 0, 16, 43, 805965), null=True),
        ),
    ]