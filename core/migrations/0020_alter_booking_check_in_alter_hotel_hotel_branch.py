# Generated by Django 4.0.6 on 2022-07-19 18:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_hotel_hotel_branch_alter_booking_check_in'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='check_in',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 19, 21, 33, 0, 470429)),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='hotel_branch',
            field=models.CharField(max_length=50),
        ),
    ]
