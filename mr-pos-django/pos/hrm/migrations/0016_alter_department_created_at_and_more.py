# Generated by Django 4.1.4 on 2022-12-30 14:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrm', '0015_alter_department_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 30, 20, 56, 52, 513161)),
        ),
        migrations.AlterField(
            model_name='designation',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 30, 20, 56, 52, 513161)),
        ),
        migrations.AlterField(
            model_name='employee',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 30, 20, 56, 52, 513161)),
        ),
        migrations.AlterField(
            model_name='employee',
            name='join_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 30, 20, 56, 52, 560111)),
        ),
        migrations.AlterField(
            model_name='employeesalarypayment',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 30, 20, 56, 52, 513161)),
        ),
        migrations.AlterField(
            model_name='employeesalarypayment',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 12, 30, 14, 56, 52, 562110, tzinfo=datetime.timezone.utc), null=True),
        ),
        migrations.AlterField(
            model_name='employeesalarypayment',
            name='salary_month_unique_for_year',
            field=models.DateField(default=datetime.datetime(2022, 12, 30, 20, 56, 52, 562110), unique=True),
        ),
    ]
