# Generated by Django 3.2.20 on 2023-07-12 19:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workshops', '0014_workshop_attendees'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workshop',
            name='attendees',
        ),
    ]
