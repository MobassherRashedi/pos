# Generated by Django 4.1.4 on 2022-12-30 21:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchases', '0017_alter_purchase_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 31, 3, 3, 42, 606907)),
        ),
        migrations.AlterField(
            model_name='purchasecart',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 31, 3, 3, 42, 606907)),
        ),
        migrations.AlterField(
            model_name='purchasecartamount',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 31, 3, 3, 42, 606907)),
        ),
    ]
