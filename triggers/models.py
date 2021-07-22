from django.db import models
from users.models import Account
from geofences.models import Geofence

ALERT_TYPE_CHOICES = [
    (1001, 'ALERTA DE PANICO'),
    (1002, 'ALERTA DE DESCONEXION DE BATERIA'),
    (1003, 'ALERTA DE VELOCIDAD'),
    (1004, 'ALERTA DE INGRESO A GEOCERCA'),
    (1005, 'ALERTA DE SALIDA DE GEOCERCA'),
    (1006, 'ALERTA DE VELOCIDAD POR GEOCERCA'),
    (1007, 'ALERTA DE PARADA EN GEOCERCA'),
]

# Create your models here.
class FleetTriggerExtension1003(models.Model):
    speed = models.IntegerField()
    account = models.ForeignKey(Account,on_delete=models.CASCADE)

class FleetTriggerExtension1006(models.Model):
    speed = models.IntegerField()
    geofences = models.ManyToManyField(Geofence)
    account = models.ForeignKey(Account,on_delete=models.CASCADE)

class FleetTriggerExtension1007(models.Model):
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
    #condition = models.TextField()
    is_active = models.BooleanField(default=True)
    send_notification = models.BooleanField(default=True)
    send_mail_notification = models.BooleanField(default=True)
    extension1003 = models.OneToOneField(FleetTriggerExtension1003,null=True,blank=True,on_delete=models.CASCADE)
    extension1006 = models.OneToOneField(FleetTriggerExtension1006,null=True,blank=True,on_delete=models.CASCADE)
    extension1007 = models.OneToOneField(FleetTriggerExtension1007,null=True,blank=True,on_delete=models.CASCADE)
    account = models.ForeignKey(Account,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    class Meta:
        unique_together = (('name','account'),)
    def __str__(self):
        return f"{self.account}_{self.name}"

