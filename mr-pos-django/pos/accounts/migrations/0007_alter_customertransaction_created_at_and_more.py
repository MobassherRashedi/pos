# Generated by Django 4.1.4 on 2022-12-14 11:47

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_user_status_alter_customertransaction_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customertransaction',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 14, 17, 47, 54, 498259)),
        ),
        migrations.AlterField(
            model_name='customertransaction',
            name='transaction_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 14, 17, 47, 54, 509253)),
        ),
        migrations.AlterField(
            model_name='suppliertransaction',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 14, 17, 47, 54, 498259)),
        ),
        migrations.AlterField(
            model_name='suppliertransaction',
            name='transaction_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 14, 17, 47, 54, 510253)),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 14, 17, 47, 54, 498259)),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='date_of_birth',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 14, 17, 47, 54, 508254), verbose_name='Date of Birth'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
