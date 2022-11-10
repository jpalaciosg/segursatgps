from django.db import models
from users.models import Account
from forwarders.models import Forwarder

# Create your models here.
class Device(models.Model):
    uniqueid = models.CharField(unique=True,max_length=20)
    #imei = models.CharField(unique=True,max_length=20)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200,blank=True)
    sim_phonenumber = models.CharField(max_length=20,blank=True)
    sim_iccid = models.CharField(max_length=20,blank=True)
    odometer = models.FloatField(default=0.0)
    note = models.TextField(blank=True)
    account = models.ForeignKey(Account,on_delete=models.CASCADE)
    last_timestamp = models.IntegerField(default=0)
    last_latitude = models.FloatField(default=0)
    last_longitude = models.FloatField(default=0)
    last_altitude = models.IntegerField(default=0)
    last_speed = models.IntegerField(default=-1)
    last_angle = models.IntegerField(default=0)
    last_movement = models.IntegerField(default=0)
    last_hours = models.IntegerField(default=0)
    last_attributes = models.TextField(blank=True,default="{}")
    last_address = models.TextField(blank=True,default="")
    previous_location = models.TextField(blank=True,default="{}")
    show_unit_name_in_map = models.BooleanField(default=True)
    show_unit_description_in_map = models.BooleanField(default=False)
    show_unit_datetime_in_map = models.BooleanField(default=False)
    is_replica = models.BooleanField(default=False)
    ignition_source = models.CharField(max_length=50,default="ignition")
    panic_source = models.CharField(max_length=50,default="panic")
    valve1_source = models.CharField(max_length=50,default="nothing")
    valve2_source = models.CharField(max_length=50,default="nothing")
    sutran_process = models.BooleanField(default=False)
    osinergmin_process = models.BooleanField(default=False)
    forwarding_enabled = models.BooleanField(default=False)
    forwarders = models.ManyToManyField(Forwarder,
        blank=True,
        #null=True,
    )
    is_parent = models.BooleanField(default=False)
    child = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    is_child = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True,null=True)
    modified = models.DateTimeField(auto_now=True)
    class Meta:
        unique_together = (("name","account"),)
    def __str__(self):
        return self.name

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

class DeviceDigitalOutput(models.Model):
    OUTPUT_EVENT_CHOICES = [
        ('MOTOR_LOCK', 'MOTOR_LOCK'),
    ]
    device = models.ForeignKey(Device,on_delete=models.CASCADE)
    output = models.PositiveIntegerField()
    output_event = models.CharField(
        max_length=50,
        choices=OUTPUT_EVENT_CHOICES,
    )
    class Meta:
        unique_together = (
            ('device','output','output_event'),
        )

class Group(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200,blank=True)
    units = models.ManyToManyField(Device)
    account = models.ForeignKey(Account,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True,null=True)
    modified = models.DateTimeField(auto_now=True)
    class Meta:
        unique_together = (("name","account"),)
    def __str__(self):
        return self.name

class LastAlert(models.Model):
    PRIORITY_CHOICES = [
        ('L', 'LOW'),
        ('M', 'MEDIUM'),
        ('H', 'HIGH'),
        ('V', 'VERY HIGH'),
    ]
    unit = models.ForeignKey(Device,on_delete=models.CASCADE,unique=True)
    #unit = models.OneToOneField(Device,on_delete=models.CASCADE)
    timestamp = models.PositiveIntegerField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    speed = models.IntegerField()
    angle = models.IntegerField()
    address = models.TextField(blank=True,default="")
    alert_type = models.IntegerField()
    alert_priority = models.CharField(
        max_length=9,
        choices=PRIORITY_CHOICES,
        default='L',
    )
    alert_description = models.CharField(max_length=400)
    account = models.ForeignKey(Account,on_delete=models.CASCADE)