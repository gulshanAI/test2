"""jyotishi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from user_management import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('user_management.urls')),  # Include app-level URLs
    path('dashboard/', include('dashboard.urls')),  # Include app-level URLs
    path('logout/', views.custom_logout, name='logout'),
    path('updateprofileview/', views.UpdateProfileView, name='updateprofileview'),
    path('updateprofile/', views.UpdateProfile, name='updateprofile'),
    path('changepassword/', views.ChangePassword, name='changepassword'),
    path('companyprofile/', views.CompanyProfileView, name='companyprofile'),
    path('updatecompanyprofile/', views.UpdateCompanyProfile, name='updatecompanyprofile'),
    path('clientmgmt/', include('clientMgmt.urls')), # Include app-level URLs
    path('jyotishimgmt/', include('jyotishiMgmt.urls')), # Include app-level URLs
    path('vastumgmt/', include('vastuMgmt.urls')),
    path('stockmgmt/', include('stockMgmt.urls')),
    path('billmgmt/', include('billMgmt.urls'))
    
    
    
    
    
]