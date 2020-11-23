from django.db import models
from users.models import Account

# Create your models here.
class Device(models.Model):
    uniqueid = models.CharField(primary_key=True,max_length=20)
    imei = models.CharField(unique=True,max_length=20)
    sim_phonenumber = models.CharField(max_length=20,null=True,blank=True)
    sim_iccid = models.CharField(max_length=20,null=True,blank=True)
    last_timestamp = models.IntegerField(default=0)
    last_latitude = models.FloatField(default=0)
    last_longitude = models.FloatField(default=0)
    last_speed = models.IntegerField(default=-1)
    last_battery_level = models.IntegerField(default=-1)
    last_address = models.CharField(max_length=400,blank=True,default="")
    created = models.DateTimeField(auto_now_add=True,null=True)
    modified = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.uniqueid

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