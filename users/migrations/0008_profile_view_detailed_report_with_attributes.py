# Generated by Django 3.1.3 on 2021-12-06 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20211201_0042'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='view_detailed_report_with_attributes',
            field=models.BooleanField(default=False),
        ),
    ]