from django.contrib import admin
from .models import Device,Unit

# Register your models here.
admin.site.register([Device,Unit])