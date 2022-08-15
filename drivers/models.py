from django.db import models
from users.models import Account

# Create your models here.
class Driver(models.Model):
    id = models.CharField(max_length=50,primary_key=True)
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    account = models.ForeignKey(Account,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.id)