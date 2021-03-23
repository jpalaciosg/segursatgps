# Generated by Django 3.1.3 on 2021-03-14 23:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('units', '0010_auto_20210126_1704'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeviceInput',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_type', models.CharField(choices=[('DIGITAL', 'DIGITAL'), ('ANALOG', 'ANALOG')], max_length=7)),
                ('input', models.PositiveIntegerField()),
                ('device', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='units.device')),
            ],
        ),
    ]
