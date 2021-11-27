from django.db import models
#from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField('email address', unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

# Create your models here.
class Account(models.Model):
    name = models.CharField(max_length=25)
    description = models.CharField(max_length=50)
    device_timeout = models.PositiveIntegerField(default=86400)
    def __str__(self):
        return self.name

from units.models import Device

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    account = models.ForeignKey(Account,on_delete=models.CASCADE)
    is_admin = models.BooleanField(default=False)
    units = models.ManyToManyField(Device,blank=True)
    report_module = models.BooleanField(default=False)
    alert_module = models.BooleanField(default=False)
    geofence_module = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.user.username