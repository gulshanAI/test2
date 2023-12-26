from django.db import models

# Create your models here.

class EtarUpay(models.Model):
    etar_upay = models.TextField()
    a_id = models.IntegerField(null=True, blank=True)  # a_id
    delete = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    
class VishesUpay(models.Model):
    vis_upay = models.TextField()
    a_id = models.IntegerField(null=True, blank=True)  # a_id
    delete = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    
class TwoD_ThreeD_Upay(models.Model):
    twod_threed_upay = models.TextField()
    a_id = models.IntegerField(null=True, blank=True)  # a_id
    delete = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    
class VishesSalla(models.Model):
    vis_salla = models.TextField()
    a_id = models.IntegerField(null=True, blank=True)  # a_id
    delete = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    
class ExtraUpay(models.Model):
    ext_upay = models.TextField()
    a_id = models.IntegerField(null=True, blank=True)  # a_id
    delete = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    
class BSNUpay(models.Model):
    bsn_upay = models.TextField()
    a_id = models.IntegerField(null=True, blank=True)  # a_id
    delete = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    
class Vastu(models.Model):
    vastu = models.TextField()
    a_id = models.IntegerField(null=True, blank=True)  # a_id
    delete = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    
class Disha(models.Model):
    disha = models.TextField()
    a_id = models.IntegerField(null=True, blank=True)  # a_id
    delete = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    
class BadalDisha(models.Model):
    badal_disha = models.TextField()
    a_id = models.IntegerField(null=True, blank=True)  # a_id
    delete = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    
class Parinam(models.Model):
    vastu_id = models.IntegerField()
    disha_id = models.IntegerField()
    parinam = models.TextField()
    a_id = models.IntegerField(null=True, blank=True)  # a_id
    delete = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

class VastuMgmt(models.Model):
   client_id = models.IntegerField(null=True, blank=True)
   date_field = models.DateField(null=True, blank=True)
   vastu_id = models.IntegerField(null=True, blank=True)
   disha_id = models.IntegerField(null=True, blank=True)
   parinam_id = models.TextField(null=True, blank=True)
   parinam = models.TextField(null=True, blank=True)
   badal_disha_id = models.IntegerField(null=True, blank=True)
   bsn_upay_id = models.TextField(null=True, blank=True)
   bsn_upay = models.TextField(null=True, blank=True)     
   etar_upay_id = models.TextField(null=True, blank=True)
   etar_upay = models.TextField(null=True, blank=True)
   vis_upay_id = models.TextField(null=True, blank=True)
   vis_upay = models.TextField(null=True, blank=True)
   twod_threed_upay_id = models.TextField(null=True, blank=True)
   twod_threed_upay = models.TextField(null=True, blank=True)
   ext_upay_id = models.TextField(null=True, blank=True)
   ext_upay = models.TextField(null=True, blank=True)
   vis_salla_id = models.TextField(null=True, blank=True)
   vis_salla = models.TextField(null=True, blank=True)
   a_id = models.IntegerField(null=True, blank=True)  # a_id 
   delete = models.IntegerField(default=0)
   created_at = models.DateTimeField(auto_now_add=True, null=True)
   updated_at = models.DateTimeField(auto_now=True, null=True)
    
    
    
    
    