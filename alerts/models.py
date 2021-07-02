from django.db import models
from users.models import Account

# Create your models here.
class Trigger(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    condition = models.TextField()
    is_active = models.BooleanField(default=True)
    account = models.ForeignKey(Account,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    class Meta:
        unique_together = (('name','account'),)
    def __str__(self):
        return f"{self.account}_{self.name}"

class Alert(models.Model):
    PRIORITY_CHOICES = [
        ('L', 'LOW'),
        ('M', 'MEDIUM'),
        ('H', 'HIGH'),
        ('V', 'VERY HIGH'),
    ]
    id = models.BigAutoField(primary_key=True)
    unitid = models.IntegerField()
    timestamp = models.PositiveIntegerField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    speed = models.IntegerField()
    angle = models.IntegerField()
    alert_type = models.CharField(max_length=400)
    alert_priority = models.CharField(
        max_length=9,
        choices=PRIORITY_CHOICES,
        default='L',
    )
    reference = models.CharField(max_length=50,blank=True)
    #account = models.ForeignKey(Account,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    class Meta:
        app_label = 'alerts'
        unique_together = (('alert_type','unitid','timestamp'),)
        indexes = [
            models.Index(fields=['unitid','timestamp',]),
            models.Index(fields=['reference','timestamp',]),
        ]

    
