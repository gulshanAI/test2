from django.db import models

# Create your models here.

class ClientDetails(models.Model):
    client_name = models.CharField(max_length=255)
    mobile = models.CharField(max_length=10)
    a_id = models.IntegerField(null=True, blank=True)  # a_id
    delete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    

