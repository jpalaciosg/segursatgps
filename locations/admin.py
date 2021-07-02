from django.contrib import admin
from .models import Location, PanderoLocation, SutranLocation

# Register your models here.
admin.site.register([Location,SutranLocation,PanderoLocation])