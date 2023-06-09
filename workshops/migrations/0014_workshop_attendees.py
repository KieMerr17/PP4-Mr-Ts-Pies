# Generated by Django 3.2.20 on 2023-07-12 19:43

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('workshops', '0013_remove_workshop_attendees'),
    ]

    operations = [
        migrations.AddField(
            model_name='workshop',
            name='attendees',
            field=models.ManyToManyField(related_name='attended_workshops', to=settings.AUTH_USER_MODEL),
        ),
    ]
