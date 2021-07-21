from django.contrib import admin
from .models import Geofence

@admin.register(Geofence)
class GeofenceAdmin(admin.ModelAdmin):
    search_fields = ['name','description',]

# Register your models here.
#admin.site.register([Geofence])