# Generated by Django 3.1.3 on 2021-05-07 15:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('units', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.account'),
        ),
        migrations.AddField(
            model_name='devicedigitaoutput',
            name='device',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='units.device'),
        ),
        migrations.AddField(
            model_name='devicedigitalinput',
            name='device',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='units.device'),
        ),
        migrations.AddField(
            model_name='device',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.account'),
        ),
        migrations.AlterUniqueTogether(
            name='group',
            unique_together={('name', 'account')},
        ),
        migrations.AlterUniqueTogether(
            name='devicedigitaoutput',
            unique_together={('device', 'output', 'output_event')},
        ),
        migrations.AlterUniqueTogether(
            name='devicedigitalinput',
            unique_together={('device', 'input', 'input_event')},
        ),
        migrations.AlterUniqueTogether(
            name='device',
            unique_together={('name', 'account')},
        ),
    ]
