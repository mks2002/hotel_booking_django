# Generated by Django 4.1.4 on 2023-02-07 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0003_bookinghotel_end_bookinghotel_start'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookinghotel',
            name='city',
            field=models.CharField(default=None, max_length=60),
        ),
        migrations.AddField(
            model_name='bookinghotel',
            name='current_cost',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='bookinghotel',
            name='hotelname',
            field=models.CharField(default=None, max_length=80),
        ),
        migrations.AddField(
            model_name='bookinghotel',
            name='state',
            field=models.CharField(default=None, max_length=60),
        ),
    ]
