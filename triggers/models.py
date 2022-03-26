from django.db import models
from users.models import Account
from geofences.models import Geofence
from mails.models import MailList

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
]

PRIORITY_CHOICES = [
    ('L', 'LOW'),
    ('M', 'MEDIUM'),
    ('H', 'HIGH'),
    ('V', 'VERY HIGH'),
]

# Create your models here.
class Extension1003(models.Model):
    speed = models.IntegerField()
    account = models.ForeignKey(Account,on_delete=models.CASCADE)

class Extension1004(models.Model):
    geofences = models.ManyToManyField(Geofence)
    account = models.ForeignKey(Account,on_delete=models.CASCADE)

class Extension1005(models.Model):
    geofences = models.ManyToManyField(Geofence)
    account = models.ForeignKey(Account,on_delete=models.CASCADE)

class Extension1006(models.Model):
    speed = models.IntegerField()
    geofences = models.ManyToManyField(Geofence)
    account = models.ForeignKey(Account,on_delete=models.CASCADE)

class Extension1007(models.Model):
    seconds = models.IntegerField()
    geofences = models.ManyToManyField(Geofence)
    account = models.ForeignKey(Account,on_delete=models.CASCADE)

class Extension1008(models.Model):
    seconds = models.IntegerField()
    geofences = models.ManyToManyField(Geofence)
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
    extension1003 = models.OneToOneField(Extension1003,null=True,blank=True,on_delete=models.CASCADE)
    extension1004 = models.OneToOneField(Extension1004,null=True,blank=True,on_delete=models.CASCADE)
    extension1005 = models.OneToOneField(Extension1005,null=True,blank=True,on_delete=models.CASCADE)
    extension1006 = models.OneToOneField(Extension1006,null=True,blank=True,on_delete=models.CASCADE)
    extension1007 = models.OneToOneField(Extension1007,null=True,blank=True,on_delete=models.CASCADE)
    extension1008 = models.OneToOneField(Extension1008,null=True,blank=True,on_delete=models.CASCADE)
    account = models.ForeignKey(Account,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.account}_{self.name}"

