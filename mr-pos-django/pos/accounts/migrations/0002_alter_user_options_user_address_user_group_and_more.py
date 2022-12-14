# Generated by Django 4.1.4 on 2022-12-13 11:54

import accounts.models
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0001_initial'),
        ('settings', '0001_initial'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'user', 'verbose_name_plural': 'User'},
        ),
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='group',
            field=models.CharField(blank=True, choices=[], max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='phone_1',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='phone_2',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True),
        ),
        migrations.CreateModel(
            name='SupplierTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=datetime.datetime(2022, 12, 13, 17, 54, 54, 86943))),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('transaction_date', models.DateTimeField(default=datetime.datetime(2022, 12, 13, 17, 54, 54, 102570))),
                ('supplier_name', models.CharField(editable=False, max_length=150)),
                ('due', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('transaction_id', models.CharField(default=accounts.models.get_transaction_id, max_length=15)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('note', models.CharField(blank=True, max_length=250, null=True)),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='settings.supplier')),
                ('transaction_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank.banktransactiontype')),
            ],
            options={
                'verbose_name': 'Supplier Transaction',
                'verbose_name_plural': 'Supplier Transaction',
            },
        ),
        migrations.CreateModel(
            name='CustomerTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=datetime.datetime(2022, 12, 13, 17, 54, 54, 86943))),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('transaction_date', models.DateTimeField(default=datetime.datetime(2022, 12, 13, 17, 54, 54, 102570))),
                ('customer_name', models.CharField(editable=False, max_length=150)),
                ('due', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('transaction_id', models.CharField(default=accounts.models.get_transaction_id, max_length=15)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('note', models.CharField(blank=True, max_length=250, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='settings.customer')),
                ('transaction_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank.banktransactiontype')),
            ],
            options={
                'verbose_name': 'Customer Transaction',
                'verbose_name_plural': 'Customer Transaction',
            },
        ),
    ]
