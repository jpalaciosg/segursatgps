from django.db import models
from users.models import Account
from geofences.models import Geofence
from mails.models import MailList
from units.models import Device

ALERT_TYPE_CHOICES = [
    (1001, 'ALERTA DE PANICO'),
    (1002, 'ALERTA DE DESCONEXION DE BATERIA'),
    (1003, 'ALERTA DE VELOCIDAD'),
    (1004, 'ALERTA DE INGRESO A GEOCERCA'),
    (1005, 'ALERTA DE SALIDA DE GEOCERCA'),
    (1006, 'ALERTA DE VELOCIDAD POR GEOCERCA'),
    (1007, 'ALERTA DE PARADA EN GEOCERCA'),
    (1008, 'ALERTA DE PARADA FUERA DE GEOCERCA'),
    (1009, 'ALERTA DE ACELERACION BRUSCA'),
    (1010, 'ALERTA DE FRENADO BRUSCO'),
    (1011, 'ALERTA DE GIRO BRUSCO'),
    (1012, 'ALERTA DE FALLA DE TRANSMISION'),
]

PRIORITY_CHOICES = [
    ('L', 'LOW'),
    ('M', 'MEDIUM'),
    ('H', 'HIGH'),
    ('V', 'VERY HIGH'),
]

# Create your models here.

# Fleet trigger models

class FleetTriggerExtension1003(models.Model):
    speed = models.IntegerField()
    account = models.ForeignKey(Account,on_delete=models.CASCADE)

class FleetTriggerExtension1004(models.Model):
    geofences = models.ManyToManyField(Geofence)
    account = models.ForeignKey(Account,on_delete=models.CASCADE)

class FleetTriggerExtension1005(models.Model):
    geofences = models.ManyToManyField(Geofence)
    account = models.ForeignKey(Account,on_delete=models.CASCADE)

class FleetTriggerExtension1006(models.Model):
    speed = models.IntegerField()
    geofences = models.ManyToManyField(Geofence)
    account = models.ForeignKey(Account,on_delete=models.CASCADE)

class FleetTriggerExtension1007(models.Model):
    seconds = models.IntegerField()
    geofences = models.ManyToManyField(Geofence)
    account = models.ForeignKey(Account,on_delete=models.CASCADE)

class FleetTriggerExtension1008(models.Model):
    seconds = models.IntegerField()
    geofences = models.ManyToManyField(Geofence)
    account = models.ForeignKey(Account,on_delete=models.CASCADE)

class FleetTriggerExtension1012(models.Model):
    seconds = models.IntegerField()
    account = models.ForeignKey(Account,on_delete=models.CASCADE)

class FleetTrigger(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    alert_type = models.IntegerField(
        choices=ALERT_TYPE_CHOICES,
    )
    alert_priority = models.CharField(
        max_length=9,
        choices=PRIORITY_CHOICES,
        default='L',
    )
    is_active = models.BooleanField(default=True)
    send_notification = models.BooleanField(default=True)
    send_mail_notification = models.BooleanField(default=True)
    mail_list = models.ForeignKey(MailList,null=True,blank=True,on_delete=models.SET_NULL)
    extension1003 = models.OneToOneField(FleetTriggerExtension1003,null=True,blank=True,on_delete=models.CASCADE)
    extension1004 = models.OneToOneField(FleetTriggerExtension1004,null=True,blank=True,on_delete=models.CASCADE)
    extension1005 = models.OneToOneField(FleetTriggerExtension1005,null=True,blank=True,on_delete=models.CASCADE)
    extension1006 = models.OneToOneField(FleetTriggerExtension1006,null=True,blank=True,on_delete=models.CASCADE)
    extension1007 = models.OneToOneField(FleetTriggerExtension1007,null=True,blank=True,on_delete=models.CASCADE)
    extension1008 = models.OneToOneField(FleetTriggerExtension1008,null=True,blank=True,on_delete=models.CASCADE)
    extension1012 = models.OneToOneField(FleetTriggerExtension1012,null=True,blank=True,on_delete=models.CASCADE)
    account = models.ForeignKey(Account,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.account}_{self.name}"

# Unit trigger models

class UnitTriggerExtension1003(models.Model):
    speed = models.IntegerField()
    account = models.ForeignKey(Account,on_delete=models.CASCADE)

class UnitTriggerExtension1004(models.Model):
    geofences = models.ManyToManyField(Geofence)
    account = models.ForeignKey(Account,on_delete=models.CASCADE)

class UnitTriggerExtension1005(models.Model):
    geofences = models.ManyToManyField(Geofence)
    account = models.ForeignKey(Account,on_delete=models.CASCADE)

class UnitTriggerExtension1006(models.Model):
    speed = models.IntegerField()
    geofences = models.ManyToManyField(Geofence)
    account = models.ForeignKey(Account,on_delete=models.CASCADE)

class UnitTriggerExtension1007(models.Model):
    seconds = models.IntegerField()
    geofences = models.ManyToManyField(Geofence)
    account = models.ForeignKey(Account,on_delete=models.CASCADE)

class UnitTriggerExtension1008(models.Model):
    seconds = models.IntegerField()
    geofences = models.ManyToManyField(Geofence)
    account = models.ForeignKey(Account,on_delete=models.CASCADE)

class UnitTrigger(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    alert_type = models.IntegerField(
        choices=ALERT_TYPE_CHOICES,
    )
    alert_priority = models.CharField(
        max_length=9,
        choices=PRIORITY_CHOICES,
        default='L',
    )
    is_active = models.BooleanField(default=True)
    send_notification = models.BooleanField(default=True)
    send_mail_notification = models.BooleanField(default=True)
    mail_list = models.ForeignKey(MailList,null=True,blank=True,on_delete=models.SET_NULL)
    units = models.ManyToManyField(Device)
    extension1003 = models.OneToOneField(UnitTriggerExtension1003,null=True,blank=True,on_delete=models.CASCADE)
    extension1004 = models.OneToOneField(UnitTriggerExtension1004,null=True,blank=True,on_delete=models.CASCADE)
    extension1005 = models.OneToOneField(UnitTriggerExtension1005,null=True,blank=True,on_delete=models.CASCADE)
    extension1006 = models.OneToOneField(UnitTriggerExtension1006,null=True,blank=True,on_delete=models.CASCADE)
    extension1007 = models.OneToOneField(UnitTriggerExtension1007,null=True,blank=True,on_delete=models.CASCADE)
    extension1008 = models.OneToOneField(UnitTriggerExtension1008,null=True,blank=True,on_delete=models.CASCADE)
    account = models.ForeignKey(Account,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.account}_{self.name}"