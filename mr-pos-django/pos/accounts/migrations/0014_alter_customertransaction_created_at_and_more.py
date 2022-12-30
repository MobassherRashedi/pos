# Generated by Django 4.1.4 on 2022-12-21 11:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_alter_customertransaction_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customertransaction',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 21, 17, 3, 22, 781344)),
        ),
        migrations.AlterField(
            model_name='customertransaction',
            name='transaction_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 21, 17, 3, 22, 806329)),
        ),
        migrations.AlterField(
            model_name='suppliertransaction',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 21, 17, 3, 22, 781344)),
        ),
        migrations.AlterField(
            model_name='suppliertransaction',
            name='transaction_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 21, 17, 3, 22, 806329)),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 21, 17, 3, 22, 781344)),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='date_of_birth',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 21, 17, 3, 22, 805329), verbose_name='Date of Birth'),
        ),
    ]