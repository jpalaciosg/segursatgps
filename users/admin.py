from django.contrib import admin
from .models import Account,User,Profile

# Register your models here.
admin.site.register([Account,User,Profile])