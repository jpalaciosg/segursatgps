from django.db import models

class Forwarder(models.Model):
    name = models.CharField(max_length=50,unique=True)
    description = models.CharField(max_length=200,blank=True)
    is_active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True,null=True)
    modified = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name