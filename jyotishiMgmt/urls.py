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


urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Url For Jyishi Management
    path('jyotishi_view/', views.jyotishiView),
    path('get_jyosalla/', views.getJyoSalla), #get Salla From Question
    path('post_jyo_rec/', views.postJyoRecord), #listing of all records
    path('get_jyo_records/', views.getJyoRecords),
    path('get_jyo_records/', views.getJyoRecords),#listing of all records
    path('jyo_mgmt_delete/<id>/', views.jyoMgmtDelete),
    path('dowload_jyotishi_pdf/<id>/', views.dowloadJyotishiPDF),
    
    
    # Url For Jyishi Questions
    path('jyotishi_que/', views.jyotishiQuestionsView),
    path('post_jyoquestions/', views.postjyoQuestions),
    path('jyo_questiondelete/<id>/', views.jyoQuestionDelete),
    
    # Url For Jyotishi Upay
    path('jyotishi_upay/', views.jyotishiUpayView),
    path('post_jyoupay/', views.postjyoUpay),
    path('jyo_upaydelete/<id>/', views.jyoUpayDelete),
    
    # Url For Jyotishi Salla
    path('jyotishi_salla/', views.jyotishiSallaView),
    path('post_jyosalla/', views.postJyoSalla),
    path('jyo_salladelete/<id>/', views.jyoSallaDelete),
    
    # Url For Vishes Salla
    path('vishes_salla/', views.vishesSallaView),
    path('post_vissalla/', views.postVisSalla),
    path('vis_salladelete/<id>/', views.visSallaDelete),
    
    # Url For Karmik Upay
    path('karmic_upay/', views.karmicUpayView),
    path('post_karupay/', views.postKarUpay),
    path('kar_upaydelete/<id>/', views.karUpayDelete)
    
    
    
    
    
    
   
    
    
   
   
    
    
    
]