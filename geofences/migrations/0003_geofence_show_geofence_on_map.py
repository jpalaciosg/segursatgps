# Generated by Django 3.1.3 on 2021-08-12 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geofences', '0002_auto_20210507_1540'),
    ]

    operations = [
        migrations.AddField(
            model_name='geofence',
            name='show_geofence_on_map',
            field=models.BooleanField(default=True),
        ),
    ]
