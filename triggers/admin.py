from django.contrib import admin
from .models import FleetTrigger,UnitTrigger,Extension1003,Extension1004,Extension1005,Extension1006,Extension1007,Extension1008

# Register your models here.
admin.site.register([
  FleetTrigger,
  UnitTrigger,
  Extension1003,
  Extension1004,
  Extension1005,
  Extension1006,
  Extension1007,
  Extension1008,
])