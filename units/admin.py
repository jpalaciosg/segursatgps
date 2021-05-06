from django.contrib import admin
from .models import Device,DeviceDigitalInput,Group

# Register your models here.
admin.site.register([Device,DeviceDigitalInput,Group])