# Generated by Django 4.1.4 on 2022-12-21 10:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrm', '0008_alter_department_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 21, 16, 3, 25, 305883)),
        ),
        migrations.AlterField(
            model_name='designation',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 21, 16, 3, 25, 305883)),
        ),
        migrations.AlterField(
            model_name='employee',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 21, 16, 3, 25, 305883)),
        ),
        migrations.AlterField(
            model_name='employee',
            name='join_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 21, 16, 3, 25, 361722)),
        ),
        migrations.AlterField(
            model_name='employeesalarypayment',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 21, 16, 3, 25, 305883)),
        ),
        migrations.AlterField(
            model_name='employeesalarypayment',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 12, 21, 10, 3, 25, 362720, tzinfo=datetime.timezone.utc), null=True),
        ),
        migrations.AlterField(
            model_name='employeesalarypayment',
            name='salary_month_unique_for_year',
            field=models.DateField(default=datetime.datetime(2022, 12, 21, 16, 3, 25, 362720), unique=True),
        ),
    ]