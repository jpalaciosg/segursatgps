from django.db import models

# Create your models here.
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
    address = models.TextField(blank=True,default="")
    alert_type = models.IntegerField()
    alert_description = models.CharField(max_length=400)
    alert_priority = models.CharField(
        max_length=9,
        choices=PRIORITY_CHOICES,
        default='L',
    )
    reference = models.CharField(max_length=50,blank=True)
    accountid = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    class Meta:
        app_label = 'alerts'
        unique_together = (('alert_type','unitid','timestamp'),)
        indexes = [
            models.Index(fields=['unitid','timestamp',]),
            models.Index(fields=['accountid','timestamp',]),
            models.Index(fields=['reference','timestamp',]),
            models.Index(fields=['unitid','alert_type','timestamp',]),
        ]

    
