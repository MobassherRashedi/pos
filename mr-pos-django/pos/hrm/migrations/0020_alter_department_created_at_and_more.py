# Generated by Django 4.1.4 on 2022-12-30 21:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrm', '0019_alter_department_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 31, 3, 8, 39, 965270)),
        ),
        migrations.AlterField(
            model_name='designation',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 31, 3, 8, 39, 965270)),
        ),
        migrations.AlterField(
            model_name='employee',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 31, 3, 8, 39, 965270)),
        ),
        migrations.AlterField(
            model_name='employee',
            name='join_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 31, 3, 8, 40, 6248)),
        ),
        migrations.AlterField(
            model_name='employeesalarypayment',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 31, 3, 8, 39, 965270)),
        ),
        migrations.AlterField(
            model_name='employeesalarypayment',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 12, 30, 21, 8, 40, 7247, tzinfo=datetime.timezone.utc), null=True),
        ),
        migrations.AlterField(
            model_name='employeesalarypayment',
            name='salary_month_unique_for_year',
            field=models.DateField(default=datetime.datetime(2022, 12, 31, 3, 8, 40, 7247), unique=True),
        ),
    ]