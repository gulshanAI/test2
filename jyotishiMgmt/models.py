from django.db import models
from clientMgmt.models import ClientDetails

# Create your models here.

class JyotishiQuestions(models.Model):
    jyo_questions = models.CharField(max_length=500)
    a_id = models.IntegerField(null=True, blank=True)  # a_id
    delete = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    
class JyotishiUpay(models.Model):
    jyo_upay = models.TextField()
    a_id = models.IntegerField(null=True, blank=True)  # a_id
    delete = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    
class JyotishiSalla(models.Model):
    jyoque_id = models.IntegerField()   # jque_id is foreign key /  we are taking this from jyotishi questions.
    jyo_salla = models.TextField()
    a_id = models.IntegerField(null=True, blank=True)  # a_id 
    delete = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    
class VishesSalla(models.Model):
    jyoque_id = models.IntegerField()   # jque_id is foreign key /  we are taking this from jyotishi questions.
    vis_salla = models.TextField()
    a_id = models.IntegerField(null=True, blank=True)  # a_id 
    delete = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    
class KarmikUpay(models.Model):
    jyoque_id = models.IntegerField()   # jque_id is foreign key /  we are taking this from jyotishi questions.
    kar_upay = models.TextField()
    a_id = models.IntegerField(null=True, blank=True)  # a_id 
    delete = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    
class JyotishiMgmt(models.Model):
    client_id = models.ForeignKey(ClientDetails, on_delete=models.CASCADE)
    date_field = models.DateField()
    jyo_que_id = models.TextField()
    jyo_questions = models.CharField(max_length=500)
    jyo_upay_id = models.TextField()
    jyo_upay = models.TextField()
    jyo_salla_id = models.TextField()
    jyo_salla = models.TextField()
    vis_salla_id = models.TextField()
    vis_salla = models.TextField()
    kar_upay_id = models.TextField()
    kar_upay = models.TextField()
    a_id = models.IntegerField(null=True, blank=True)  # a_id 
    delete = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    
    
    
    
    
    
    

    
    

    




