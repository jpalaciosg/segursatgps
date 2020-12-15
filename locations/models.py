from django.db import models

# Create your models here.
class Location(models.Model):
    id = models.BigAutoField(primary_key=True)
    unit_name = models.CharField(max_length=50)
    timestamp = models.PositiveIntegerField(default=0)
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)
    angle = models.IntegerField(default=-1)
    speed = models.IntegerField(default=-1)
    satellites = models.PositiveSmallIntegerField(default=0)
    ignition = models.BooleanField(default=False)
    panic = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

