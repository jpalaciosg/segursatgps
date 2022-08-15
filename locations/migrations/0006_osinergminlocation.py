# Generated by Django 3.1.3 on 2022-01-29 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0005_auto_20210702_2031'),
    ]

    operations = [
        migrations.CreateModel(
            name='OsinergminLocation',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('protocol', models.CharField(max_length=100)),
                ('unitid', models.IntegerField()),
                ('timestamp', models.PositiveIntegerField(default=0)),
                ('latitude', models.FloatField(default=0.0)),
                ('longitude', models.FloatField(default=0.0)),
                ('altitude', models.IntegerField(default=0)),
                ('speed', models.IntegerField(default=-1)),
                ('angle', models.IntegerField(default=-1)),
                ('attributes', models.TextField(default='')),
                ('address', models.TextField(default='')),
                ('reference', models.CharField(blank=True, max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
