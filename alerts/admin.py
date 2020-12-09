from django.contrib import admin
from .models import Trigger,Alert

# Register your models here.
admin.site.register([Trigger,Alert])