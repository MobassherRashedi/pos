# Generated by Django 4.1.4 on 2022-12-30 21:03

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0018_alter_product_created_at_alter_product_product_code_and_more'),
        ('sales', '0017_alter_sales_created_at_alter_sales_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sales',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 31, 3, 3, 42, 606907)),
        ),
        migrations.AlterField(
            model_name='sales',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 12, 31, 3, 3, 42, 640350), null=True, verbose_name='date'),
        ),
        migrations.AlterField(
            model_name='salescart',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 31, 3, 3, 42, 606907)),
        ),
        migrations.RemoveField(
            model_name='salescart',
            name='product',
        ),
        migrations.AlterField(
            model_name='salescartamount',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 31, 3, 3, 42, 606907)),
        ),
        migrations.AddField(
            model_name='salescart',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.product'),
        ),
    ]
