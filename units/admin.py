from django.contrib import admin
from .models import Device,DeviceDigitalInput

# Register your models here.
admin.site.register([Device,DeviceDigitalInput])