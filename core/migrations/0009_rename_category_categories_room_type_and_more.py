# Generated by Django 4.0.6 on 2022-07-18 23:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_booking_check_in_alter_room_hotel_location'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categories',
            old_name='category',
            new_name='room_type',
        ),
        migrations.RenameField(
            model_name='room',
            old_name='room_category',
            new_name='category',
        ),
        migrations.AlterField(
            model_name='booking',
            name='check_in',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 19, 2, 3, 42, 268423)),
        ),
    ]
