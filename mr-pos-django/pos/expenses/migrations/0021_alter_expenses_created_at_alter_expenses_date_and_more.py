# Generated by Django 4.1.4 on 2022-12-30 21:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0020_alter_expenses_created_at_alter_expenses_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expenses',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 31, 3, 11, 29, 480857)),
        ),
        migrations.AlterField(
            model_name='expenses',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 31, 3, 11, 29, 520815), null=True),
        ),
        migrations.AlterField(
            model_name='expensescatagory',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 31, 3, 11, 29, 480857)),
        ),
        migrations.AlterField(
            model_name='expensessubcatagory',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 31, 3, 11, 29, 480857)),
        ),
    ]
