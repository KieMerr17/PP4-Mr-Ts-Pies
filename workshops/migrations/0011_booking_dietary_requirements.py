# Generated by Django 3.2.19 on 2023-05-26 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workshops', '0010_booking_spaces'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='dietary_requirements',
            field=models.IntegerField(choices=[(0, 'No Special Requirement'), (1, 'Vegetarian'), (2, 'Pescetarian'), (3, 'Vegan'), (4, 'Nut Allergy')], default=0),
        ),
    ]
