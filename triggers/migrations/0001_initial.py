# Generated by Django 3.1.3 on 2021-09-04 18:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('geofences', '0003_geofence_show_geofence_on_map'),
        ('users', '0003_auto_20210812_1556'),
    ]

    operations = [
        migrations.CreateModel(
            name='FleetTriggerExtension1008',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seconds', models.IntegerField()),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.account')),
                ('geofences', models.ManyToManyField(to='geofences.Geofence')),
            ],
        ),
        migrations.CreateModel(
            name='FleetTriggerExtension1007',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seconds', models.IntegerField()),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.account')),
                ('geofences', models.ManyToManyField(to='geofences.Geofence')),
            ],
        ),
        migrations.CreateModel(
            name='FleetTriggerExtension1006',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('speed', models.IntegerField()),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.account')),
                ('geofences', models.ManyToManyField(to='geofences.Geofence')),
            ],
        ),
        migrations.CreateModel(
            name='FleetTriggerExtension1003',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('speed', models.IntegerField()),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.account')),
            ],
        ),
        migrations.CreateModel(
            name='FleetTrigger',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
                ('alert_type', models.IntegerField(choices=[(1001, 'ALERTA DE PANICO'), (1002, 'ALERTA DE DESCONEXION DE BATERIA'), (1003, 'ALERTA DE VELOCIDAD'), (1004, 'ALERTA DE INGRESO A GEOCERCA'), (1005, 'ALERTA DE SALIDA DE GEOCERCA'), (1006, 'ALERTA DE VELOCIDAD POR GEOCERCA'), (1007, 'ALERTA DE PARADA EN GEOCERCA'), (1008, 'ALERTA DE PARADA FUERA DE GEOCERCA')])),
                ('is_active', models.BooleanField(default=True)),
                ('send_notification', models.BooleanField(default=True)),
                ('send_mail_notification', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.account')),
                ('extension1003', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='triggers.fleettriggerextension1003')),
                ('extension1006', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='triggers.fleettriggerextension1006')),
                ('extension1007', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='triggers.fleettriggerextension1007')),
                ('extension1008', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='triggers.fleettriggerextension1008')),
            ],
            options={
                'unique_together': {('name', 'account')},
            },
        ),
    ]
