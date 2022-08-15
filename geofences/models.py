from django.db import models
from users.models import Account

# Create your models here.
class Geofence(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    geojson = models.TextField()
    show_geofence_on_map = models.BooleanField(default=True)
    account = models.ForeignKey(Account,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.account}_{self.name}"

class GeofenceGroup(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200,blank=True)
    geofences = models.ManyToManyField(Geofence)
    account = models.ForeignKey(Account,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True,null=True)
    modified = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name