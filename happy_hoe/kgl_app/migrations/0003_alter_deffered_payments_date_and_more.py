# Generated by Django 5.0.6 on 2024-09-07 14:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kgl_app', '0002_sales_branch_name_alter_deffered_payments_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deffered_payments',
            name='date',
            field=models.DateField(default=datetime.datetime(2024, 9, 7, 17, 33, 8, 517107)),
        ),
        migrations.AlterField(
            model_name='deffered_payments',
            name='date_of_payment',
            field=models.DateField(default=datetime.datetime(2024, 9, 7, 17, 33, 8, 517107)),
        ),
        migrations.AlterField(
            model_name='sales',
            name='date',
            field=models.DateField(default=datetime.datetime(2024, 9, 7, 17, 33, 8, 517107)),
        ),
    ]
