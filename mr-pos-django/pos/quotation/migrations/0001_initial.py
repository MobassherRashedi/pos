# Generated by Django 4.1.4 on 2022-12-14 06:56

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import quotation.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('settings', '0002_delete_userinfo_alter_catagory_created_at_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuotationCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=datetime.datetime(2022, 12, 14, 12, 56, 52, 637162))),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('quantity', models.IntegerField()),
                ('sales_rate', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('total_amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='settings.customer')),
            ],
            options={
                'verbose_name': 'Quotation Cart',
                'verbose_name_plural': 'Quotation Cart',
            },
        ),
        migrations.CreateModel(
            name='QuotationCartAmount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=datetime.datetime(2022, 12, 14, 12, 56, 52, 637162))),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('sub_total', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('vat', models.DecimalField(decimal_places=2, default=0.0, max_digits=4)),
                ('vat_amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('discount', models.DecimalField(decimal_places=2, default=0.0, max_digits=4)),
                ('discount_amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('cart', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='quotation.quotationcart')),
            ],
            options={
                'verbose_name': 'Quotation Cart Amount',
                'verbose_name_plural': 'Quotation Cart Amount',
            },
        ),
        migrations.CreateModel(
            name='Quotation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=datetime.datetime(2022, 12, 14, 12, 56, 52, 637162))),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('invoice_no', models.CharField(default=quotation.models.get_invoice_number, editable=False, max_length=15)),
                ('customer_name', models.CharField(max_length=150)),
                ('phone', models.CharField(blank=True, max_length=16, null=True)),
                ('address', models.CharField(blank=True, max_length=150, null=True)),
                ('sales_rate', models.DecimalField(decimal_places=2, max_digits=10)),
                ('qty', models.PositiveIntegerField()),
                ('stock', models.PositiveIntegerField()),
                ('totla_for_specific_item', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('returened', models.BooleanField(default=False)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
                ('purchased_by', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Quotation',
                'verbose_name_plural': 'Quotation',
            },
        ),
    ]
