from django.db import models
from users.models import Account

ALERT_TYPE_CHOICES = [
    (1001, 'ALERTA DE PANICO'),
    (1002, 'ALERTA DE DESCONEXION DE BATERIA'),
    (1003, 'ALERTA DE VELOCIDAD'),
    (1004, 'ALERTA DE INGRESO A GEOCERCA'),
    (1005, 'ALERTA DE SALIDA DE GEOCERCA'),
    (1006, 'ALERTA DE VELOCIDAD POR GEOCERCA'),
]

# Create your models here.
class FleetTrigger(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    alert_type = models.IntegerField(
        choices=ALERT_TYPE_CHOICES,
    )
    condition = models.TextField()
    is_active = models.BooleanField(default=True)
    send_notification = models.BooleanField(default=True)
    send_mail_notification = models.BooleanField(default=True)
    account = models.ForeignKey(Account,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    class Meta:
        unique_together = (('name','account'),)
    def __str__(self):
        return f"{self.account}_{self.name}"