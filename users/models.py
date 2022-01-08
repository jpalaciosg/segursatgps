from django.db import models
#from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField('email address',blank=True)
    description = models.CharField(max_length=100,blank=True)
    #USERNAME_FIELD = 'email'
    #REQUIRED_FIELDS = ['username']

# Create your models here.
class Account(models.Model):
    name = models.CharField(max_length=25,unique=True)
    description = models.CharField(max_length=50)
    device_timeout = models.PositiveIntegerField(default=86400)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
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
    # privileges
    view_detailed_report = models.BooleanField(default=False)
    view_speed_report = models.BooleanField(default=False)
    view_stop_report = models.BooleanField(default=False)
    view_trip_report = models.BooleanField(default=False)
    view_mileage_report = models.BooleanField(default=False)
    view_geofence_report = models.BooleanField(default=False)
    view_driving_style_report = models.BooleanField(default=False)
    view_telemetry_report = models.BooleanField(default=False)
    view_detailed_report_with_attributes = models.BooleanField(default=False)
    view_group_trip_report = models.BooleanField(default=False)
    view_group_speed_report = models.BooleanField(default=False)
    view_group_mileage_report = models.BooleanField(default=False)
    view_group_stop_report = models.BooleanField(default=False)
    view_group_geofence_report = models.BooleanField(default=False)
    view_units = models.BooleanField(default=False)
    view_triggers = models.BooleanField(default=False)
    view_geofences = models.BooleanField(default=False)
    view_users = models.BooleanField(default=False)
    view_latest_alerts = models.BooleanField(default=False)
    view_alert_history = models.BooleanField(default=False)
    # fin - privileges
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.user.username

class AdminProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.user.username