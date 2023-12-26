from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from django.core.files.storage import FileSystemStorage
from django.conf import settings

fs = FileSystemStorage(location=settings.MEDIA_ROOT)


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Please provide the email number')
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, **extra_fields)
    
class AuthUser(AbstractUser):
    username = None
    first_name = None
    last_name = None
    name = models.CharField(max_length=55, blank=True, null=True)
    email = models.EmailField(
        max_length=150, blank=True, null=True, unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def createUser(data):
        try:
            user = AuthUser.objects.get(email=data.email)
            return user
        except ObjectDoesNotExist:
            user = AuthUser.objects.create(
                email=data.email,
            )
        return user

    objects = UserManager()

    def __str__(self):
        return str(self.name)


class CompanyProfileModel(models.Model):
    company_name = models.CharField(max_length=255)
    website = models.CharField(max_length=255)
    company_email = models.EmailField()
    account_email = models.EmailField()
    address = models.TextField()
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    pincode = models.IntegerField()
    pan_number = models.CharField(max_length=255)
    # pan_file = models.CharField(max_length=255, blank=True, null=True)
    gst_number = models.CharField(max_length=255)
    # gst_file = models.CharField(max_length=255, blank=True, null=True)
    iec_code = models.CharField(max_length=255)
    # logo = models.CharField(max_length=255, blank=True, null=True)
    iso_certificate_number = models.CharField(max_length=255)
    # iso_file = models.CharField(max_length=255, blank=True, null=True)
    primary_mobile = models.CharField(max_length=255)
    alternate_mobile = models.CharField(max_length=255)
    account_name = models.CharField(max_length=255)
    account_number = models.CharField(max_length=255)
    branch = models.CharField(max_length=255)
    bank_name = models.CharField(max_length=255)
    ifsc_code = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    pan_file = models.FileField(storage=fs, upload_to='company', null=True)
    gst_file = models.FileField(storage=fs, upload_to='company', null=True)
    logo_file = models.FileField(storage=fs, upload_to='company', null=True)
    iso_file = models.FileField(storage=fs, upload_to='company', null=True)
    
    
   
    
    

