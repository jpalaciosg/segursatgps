from django.db import models
from users.models import Account

# Create your models here.
class MailList(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    mails = models.TextField(blank=True)
    account = models.ForeignKey(Account,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    class Meta:
        unique_together = (('name','account'),)
    def __str__(self):
        return f"{self.account}_{self.name}"

