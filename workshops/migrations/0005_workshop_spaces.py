# Generated by Django 3.2.19 on 2023-05-26 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workshops', '0004_auto_20230526_1210'),
    ]

    operations = [
        migrations.AddField(
            model_name='workshop',
            name='spaces',
            field=models.IntegerField(default=6),
        ),
    ]