from django.contrib import admin
from .models import MailList,AlertMailQueue

# Register your models here.
admin.site.register([
  MailList,
  AlertMailQueue,
])