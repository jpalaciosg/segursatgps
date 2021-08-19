from django.contrib import admin
from .models import FleetTrigger,FleetTriggerExtension1003,FleetTriggerExtension1006,FleetTriggerExtension1007,FleetTriggerExtension1008

# Register your models here.
admin.site.register([
  FleetTrigger,
  FleetTriggerExtension1003,
  FleetTriggerExtension1006,
  FleetTriggerExtension1007,
  FleetTriggerExtension1008,
])