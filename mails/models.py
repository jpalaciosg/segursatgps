from statistics import mode
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

class AlertMailQueue(models.Model):
    alert_description = models.TextField(blank=True)
    alert_timestamp = models.IntegerField()
    alert_latitude = models.FloatField
    alert_longitude = models.FloatField
    alert_speed = models.IntegerField()
    alert_angle = models.IntegerField()
    alert_address = models.TextField(blank=True)
    unit_name = models.CharField(max_length=50)
    unit_description = models.CharField(max_length=50)
    account_id = models.IntegerField()
    customer_description = models.TextField(blank=True)
    mails = models.TextField(blank=True)
    it_was_sent = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    class Meta:
        # indexes
        indexes = [
            models.Index(fields=['account_id', 'alert_timestamp',]),
        ]