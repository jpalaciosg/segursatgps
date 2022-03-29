from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register([
  FleetTrigger,
  FleetTriggerExtension1003,
  FleetTriggerExtension1004,
  FleetTriggerExtension1005,
  FleetTriggerExtension1006,
  FleetTriggerExtension1007,
  FleetTriggerExtension1008,
  UnitTriggerExtension1003,
  UnitTrigger,
])