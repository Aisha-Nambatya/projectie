# Generated by Django 5.0.6 on 2024-09-08 20:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kgl_app', '0006_alter_deffered_payments_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deffered_payments',
            name='date',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='deffered_payments',
            name='date_of_payment',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='sales',
            name='date',
            field=models.DateField(default=datetime.datetime(2024, 9, 8, 23, 17, 54, 343121)),
        ),
    ]
