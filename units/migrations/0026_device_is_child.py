# Generated by Django 3.1.3 on 2022-11-10 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('units', '0025_remove_device_imei'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='is_child',
            field=models.BooleanField(default=False),
        ),
    ]