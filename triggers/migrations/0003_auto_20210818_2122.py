# Generated by Django 3.1.3 on 2021-08-18 21:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('geofences', '0003_geofence_show_geofence_on_map'),
        ('users', '0003_auto_20210812_1556'),
        ('triggers', '0002_auto_20210722_2037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fleettrigger',
            name='alert_type',
            field=models.IntegerField(choices=[(1001, 'ALERTA DE PANICO'), (1002, 'ALERTA DE DESCONEXION DE BATERIA'), (1003, 'ALERTA DE VELOCIDAD'), (1004, 'ALERTA DE INGRESO A GEOCERCA'), (1005, 'ALERTA DE SALIDA DE GEOCERCA'), (1006, 'ALERTA DE VELOCIDAD POR GEOCERCA'), (1007, 'ALERTA DE PARADA EN GEOCERCA'), (1008, 'ALERTA DE PARADA FUERA DE GEOCERCA')]),
        ),
        migrations.CreateModel(
            name='FleetTriggerExtension1008',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seconds', models.IntegerField()),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.account')),
                ('geofences', models.ManyToManyField(to='geofences.Geofence')),
            ],
        ),
        migrations.AddField(
            model_name='fleettrigger',
            name='extension1008',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='triggers.fleettriggerextension1008'),
        ),
    ]
