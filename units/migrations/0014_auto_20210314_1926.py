# Generated by Django 3.1.3 on 2021-03-15 00:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('units', '0013_auto_20210314_1919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deviceinput',
            name='device',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='units.device'),
        ),
        migrations.AlterUniqueTogether(
            name='deviceinput',
            unique_together={('device', 'device_type', 'input')},
        ),
    ]
