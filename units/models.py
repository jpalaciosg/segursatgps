from django.db import models
from users.models import Account

# Create your models here.
class Device(models.Model):
    uniqueid = models.CharField(primary_key=True,max_length=20)
    imei = models.CharField(unique=True,max_length=20)
    sim_phonenumber = models.CharField(max_length=20,blank=True)
    sim_iccid = models.CharField(max_length=20,blank=True)
    last_timestamp = models.IntegerField(default=0)
    last_latitude = models.FloatField(default=0)
    last_longitude = models.FloatField(default=0)
    last_altitude = models.IntegerField(default=0)
    last_speed = models.IntegerField(default=-1)
    last_angle = models.IntegerField(default=0)
    last_attributes = models.TextField(default="")
    last_gps_odometer = models.FloatField(default=0.0)
    last_address = models.TextField(default="")
    previous_location = models.TextField(default="")
    created = models.DateTimeField(auto_now_add=True,null=True)
    modified = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.uniqueid

class DeviceDigitalInput(models.Model):
    INPUT_EVENT_CHOICES = [
        ('IGNITION', 'IGNITION'),
        ('PANIC', 'PANIC'),
    ]
    device = models.ForeignKey(Device,on_delete=models.CASCADE)
    input = models.PositiveIntegerField()
    input_event = models.CharField(
        max_length=50,
        choices=INPUT_EVENT_CHOICES,
    )
    class Meta:
        unique_together = (
            ('device','input','input_event'),
        )

class Unit(models.Model):
    name = models.CharField(max_length=50)
    device = models.OneToOneField(Device,on_delete=models.CASCADE)
    account = models.ForeignKey(Account,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    class Meta:
        unique_together = (("name","account"),)
    def __str__(self):
        return self.name