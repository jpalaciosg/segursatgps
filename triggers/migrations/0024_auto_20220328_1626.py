# Generated by Django 3.1.3 on 2022-03-28 16:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0018_user_description'),
        ('geofences', '0003_geofence_show_geofence_on_map'),
        ('triggers', '0023_auto_20220328_1543'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Extension1008',
            new_name='FleetTriggerExtension1008',
        ),
    ]
