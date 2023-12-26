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
from django.urls import path
from jyotishiMgmt import views
from vastuMgmt import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Url For Vastu Management
    path('vastu_mgmt_view/', views.vastuMgmtView),
    path('get_parinam/', views.getParinam),
    path('post_vastu_rec/', views.postVastuRecord),
    path('get_vastu_rec/', views.getVastuRecords),
    path('vastu_mgmt_delete/<id>/', views.vastuMgmtDelete),
    path('dowload_vastu_pdf/<id>/', views.dowloadVastuPDF),
    
    
    # Url For Etar Upay
    path('etar_upay/', views.etarUpayView),
    path('post_etarupay/', views.postEtarUpay),
    path('etar_upaydelete/<id>/', views.etarUpayDelete),
    
    # Url For Vishes Upay
    path('vishes_upay/', views.vishesUpayView),
    path('post_visupay/', views.postVisUpay),
    path('vis_upaydelete/<id>/', views.visUpayDelete),
    
    # Url For 2D 3D Upay
    path('twod_threed_upay/', views.twoDthreeDUpayView),
    path('post_twod_threed_upay/', views.posttwoDthreeDUpay),
    path('twod_threed_upaydelete/<id>/', views.twoDthreeDUpayDelete),
    
    # Url For Vishes Salla
    path('vishes_salla/', views.vishesSallaView),
    path('post_vissalla/', views.postVisSalla),
    path('vis_salladelete/<id>/', views.visSallaDelete),
    
    # Url For Extra Upay
    path('extra_upay/', views.extraUpayView),
    path('post_extupay/', views.postExtUpay),
    path('ext_upaydelete/<id>/', views.extUpayDelete),
    
    # Url For Badal Shakya Naslyas Upay
    path('bsn_upay/', views.bsnUpayView),
    path('post_bsnupay/', views.postBsnUpay),
    path('bsn_upaydelete/<id>/', views.bsnUpayDelete),
    
    # Url For Vastu
    path('vastu_view/', views.vastuView),
    path('post_vastu_view/', views.postVastu),
    path('vastu_delete/<id>/', views.vastuDelete),
    
    # Url For Disha
    path('disha_view/', views.dishaView),
    path('post_disha_view/', views.postDisha),
    path('disha_delete/<id>/', views.dishaDelete),
    
    # Url For Badal Disha
    path('badaldisha_view/', views.badalDishaView),
    path('post_badaldisha_view/', views.postBadalDisha),
    path('disha_badaldelete/<id>/', views.badalDishaDelete),
    
    # Url For Parinam
    path('parinam_view/', views.parinamView),
    path('post_parinam/', views.postParinam),
    path('parinam_delete/<id>/', views.parinamDelete)
    
    
    
    
    
    
    
    
   
    
    
   
   
    
    
    
]