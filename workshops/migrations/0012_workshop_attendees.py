# Generated by Django 3.2.19 on 2023-06-01 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workshops', '0011_booking_dietary_requirements'),
    ]

    operations = [
        migrations.AddField(
            model_name='workshop',
            name='attendees',
            field=models.ManyToManyField(blank=True, related_name='workshops_attending', to='workshops.Booking'),
        ),
    ]
