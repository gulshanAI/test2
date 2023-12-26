from django.db import models

# Create your models here.

class ProductType(models.Model):
    product_type = models.CharField(max_length=500)
    a_id = models.IntegerField(null=True, blank=True)  # a_id
    delete = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    
class ProductName(models.Model):
    protype_id = models.IntegerField()   # jque_id is foreign key /  we are taking this from jyotishi questions.
    product_name = models.CharField(max_length=500)
    a_id = models.IntegerField(null=True, blank=True)  # a_id 
    delete = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    
class CompanyName(models.Model):
    protype_id = models.IntegerField()          # Foreign key of ProductType model id
    proname_id = models.IntegerField()         # Foreign key of ProductName model id
    company_name = models.TextField()
    a_id = models.IntegerField(null=True, blank=True)  # a_id
    delete = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

class StockMgmt(models.Model):
    protype_id = models.IntegerField()
    proname_id = models.IntegerField()              # Foreign key of ProductName model id
    comname_id = models.IntegerField()          
    stock_type = models.CharField(max_length=50)
    dealer_name = models.CharField(max_length=100)
    dealer_mob_number = models.CharField(max_length=10, null=True, blank=True)
    dealer_address = models.TextField()
    date = models.DateField()
    product_weight = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    product_quantity = models.IntegerField()
    purchase_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    a_id = models.IntegerField(null=True, blank=True)  # a_id 
    delete = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    