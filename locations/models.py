from django.db import models
from django.db.models.fields import BigAutoField, BigIntegerField

# Create your models here.
class Location(models.Model):
    id = models.BigAutoField(primary_key=True)
    protocol = models.CharField(max_length=100)
    unitid = models.IntegerField()
    timestamp = models.PositiveIntegerField(default=0)
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)
    altitude = models.IntegerField(default=0)
    speed = models.IntegerField(default=-1)
    angle = models.IntegerField(default=-1)
    attributes = models.TextField(default="")
    address = models.TextField(default="")
    reference = models.CharField(max_length=50,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    class Meta:
        # app_label helps django to recognize your db
        app_label = 'locations'
        # indexes
        indexes = [
            models.Index(fields=['unitid', 'timestamp',]),
        ]
        unique_together = (
            ('unitid','timestamp',),
            #('reference','timestamp')
        )

class PanderoLocation(models.Model):
    id = models.BigAutoField(primary_key=True)
    protocol = models.CharField(max_length=100)
    unitid = models.IntegerField()
    timestamp = models.PositiveIntegerField(default=0)
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)
    altitude = models.IntegerField(default=0)
    speed = models.IntegerField(default=-1)
    angle = models.IntegerField(default=-1)
    attributes = models.TextField(default="")
    address = models.TextField(default="")
    reference = models.CharField(max_length=50,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    class Meta:
        # app_label helps django to recognize your db
        app_label = 'locations'
        # indexes
        indexes = [
            models.Index(fields=['unitid', 'timestamp',]),
        ]
        unique_together = (
            ('unitid','timestamp',),
            ('reference','timestamp')
        )

class SutranLocation(models.Model):
    id = models.BigAutoField(primary_key=True)
    unit_name = models.CharField(max_length=100)
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)
    angle = models.IntegerField(default=-1)
    speed = models.IntegerField(default=-1)
    event = models.CharField(max_length=2)
    device_datetime = models.DateTimeField()
    server_datetime = models.DateTimeField()
    status = BigIntegerField(default=0)
    sutran_process = models.IntegerField(default=0)
    class Meta:
        # app_label helps django to recognize your db
        app_label = 'locations'

class OsinergminLocation(models.Model):
    id = models.BigAutoField(primary_key=True)
    protocol = models.CharField(max_length=100)
    unitid = models.IntegerField()
    timestamp = models.PositiveIntegerField(default=0)
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)
    altitude = models.IntegerField(default=0)
    speed = models.IntegerField(default=-1)
    angle = models.IntegerField(default=-1)
    attributes = models.TextField(default="")
    address = models.TextField(default="")
    reference = models.CharField(max_length=50,blank=True)
    it_was_sent = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    class Meta:
        # app_label helps django to recognize your db
        app_label = 'locations'

class SutranPointsOfInterest(models.Model):
    name = models.CharField(max_length=50,unique=True)
    description = models.CharField(max_length=100,blank=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)