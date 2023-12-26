from .models import AuthUser
from django import forms
from django.contrib.auth.forms import AuthenticationForm

class CustomUserLoginForm(AuthenticationForm):
    class Meta:
        model = AuthUser