from django.contrib import admin
from .models import Device,DeviceDigitalInput,Unit

# Register your models here.
admin.site.register([Device,DeviceDigitalInput,Unit])