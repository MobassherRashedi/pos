# Generated by Django 4.1.4 on 2022-12-14 06:56

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IncomeCatagory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=datetime.datetime(2022, 12, 14, 12, 56, 52, 637162))),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name': 'Income Catagory',
                'verbose_name_plural': 'Income Catagory',
            },
        ),
        migrations.CreateModel(
            name='IncomeSubCatagory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=datetime.datetime(2022, 12, 14, 12, 56, 52, 637162))),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=150)),
                ('catagory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='income.incomecatagory')),
            ],
            options={
                'verbose_name': 'Income Sub Catagory',
                'verbose_name_plural': 'Income Sub Catagory',
            },
        ),
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=datetime.datetime(2022, 12, 14, 12, 56, 52, 637162))),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=150)),
                ('date', models.DateTimeField(default=datetime.datetime(2022, 12, 14, 12, 56, 52, 668122), null=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('note', models.CharField(blank=True, max_length=250, null=True)),
                ('catagory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='income.incomecatagory')),
                ('sub_catagory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='income.incomesubcatagory')),
            ],
            options={
                'verbose_name': 'Income',
                'verbose_name_plural': 'Income',
            },
        ),
    ]
