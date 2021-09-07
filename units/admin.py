from django.contrib import admin
from .models import Device,DeviceDigitalInput,Group,LastAlert

# Register your models here.
admin.site.register([Device,DeviceDigitalInput,Group,LastAlert])