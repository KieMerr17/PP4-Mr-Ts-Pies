# Generated by Django 3.2.19 on 2023-05-26 13:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('workshops', '0005_workshop_spaces'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='approved',
        ),
        migrations.AlterField(
            model_name='booking',
            name='workshop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='workshop', to='workshops.workshop'),
        ),
        migrations.AlterField(
            model_name='workshop',
            name='chef',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_chef', to=settings.AUTH_USER_MODEL),
        ),
    ]