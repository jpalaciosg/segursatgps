# Generated by Django 3.1.3 on 2021-03-17 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('units', '0019_delete_devicedigitalinput'),
    ]

    operations = [
        migrations.AddField(
            model_name='devicedigitalio',
            name='input_event',
            field=models.CharField(choices=[('UNKNOWN', 'UNKNOWN'), ('IGNITION', 'IGNITION'), ('PANIC', 'PANIC')], default='UNKNOWN', max_length=50),
        ),
    ]
