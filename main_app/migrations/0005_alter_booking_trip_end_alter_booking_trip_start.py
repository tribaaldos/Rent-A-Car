# Generated by Django 4.2.2 on 2023-06-16 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_alter_booking_trip_end'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='trip_end',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='booking',
            name='trip_start',
            field=models.DateField(),
        ),
    ]
