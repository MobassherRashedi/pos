# Generated by Django 4.1.4 on 2022-12-20 10:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('damages', '0006_alter_damages_created_at_alter_damages_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='damages',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 20, 16, 43, 56, 539266)),
        ),
        migrations.AlterField(
            model_name='damages',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 20, 16, 43, 56, 586137), null=True),
        ),
    ]
