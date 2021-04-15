from django.db import models
from users.models import Account
from units.models import Device

# Create your models here.
class MaintenaceTrigger(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    unit = models.ForeignKey(Device,on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    programing_type = models.CharField(max_length=100)
    programing = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    account = models.ForeignKey(Account,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    class Meta:
        unique_together = (('name','account'),)
    def __str__(self):
        return f"{self.account}_{self.name}"