# Generated by Django 3.1.3 on 2021-11-27 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20210915_1544'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='device_timeout',
            field=models.PositiveIntegerField(default=86400),
        ),
    ]