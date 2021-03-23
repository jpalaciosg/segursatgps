from django.db import models

# Create your models here.
class Location(models.Model):
    id = models.BigAutoField(primary_key=True)
    unit_name = models.CharField(max_length=50)
    timestamp = models.PositiveIntegerField(default=0)
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)
    altitude = models.IntegerField(default=0)
    speed = models.IntegerField(default=-1)
    angle = models.IntegerField(default=-1)
    attributes = models.TextField(default="")
    address = models.TextField(default="")
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)