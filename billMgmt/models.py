from django.db import models

# Create your models here.

class BillMgmt(models.Model):
    client_id = models.IntegerField()
    date = models.DateField(null=True, blank=True)
    total_bill_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    a_id = models.IntegerField(null=True, blank=True)  # a_id 
    delete = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    
class BillItem(models.Model):
    bill_id = models.IntegerField()
    protype_id = models.IntegerField()
    proname_id = models.IntegerField()
    comname_id = models.IntegerField()
    product_weight = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    product_units = models.CharField(max_length=20, null=True, blank=True)
    product_quantity = models.IntegerField()
    sell_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    ret_validity = models.CharField(max_length=100)
    ret_percentage = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    ret_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    exc_validity = models.CharField(max_length=100)
    exc_percentage = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    exc_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    a_id = models.IntegerField(null=True, blank=True)  # a_id 
    delete = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
