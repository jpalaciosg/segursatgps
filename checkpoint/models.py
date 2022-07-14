from django.db import models
from users.models import Account
from geofences.models import Geofence

# Create your models here.
class ControlSet(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200,blank=True)
    geofences = models.ManyToManyField(Geofence)
    account = models.ForeignKey(Account,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True,null=True)
    modified = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.account}_{self.name}"