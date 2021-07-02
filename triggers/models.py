from django.db import models
from users.models import Account

# Create your models here.
class TriggerA(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    condition = models.TextField()
    is_active = models.BooleanField(default=True)
    account = models.ForeignKey(Account,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    class Meta:
        unique_together = (('name','account'),)
    def __str__(self):
        return f"{self.account}_{self.name}"