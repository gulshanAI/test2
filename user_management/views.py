from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import CustomUserLoginForm
from .models import AuthUser, CompanyProfileModel
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password
from django.conf import settings
from pathlib import Path
import os
import shutil

# def custom_login(request):
#     if request.method == 'POST':
#         form = CustomUserLoginForm(request, request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             return redirect('dashboard/dashboard')  # Replace 'home' with your desired redirect URL
#     else:
#         form = CustomUserLoginForm()
#     print(form.errors) 
#     return render(request, 'registration/login.html', {'form': form})

def custom_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                # Store user ID in session
                request.session['user_id'] = user.id
                request.session['name'] = user.name
                return redirect('dashboard/dashboard')  # Redirect to user's profile page
            else:
                form = CustomUserLoginForm()
            print(form.errors) 
            return render(request, 'registration/login.html', {'form': form})
        else:
            form = CustomUserLoginForm()
        print(form.errors) 
        return render(request, 'registration/login.html', {'form': form})
    else:
        form = CustomUserLoginForm()
    print(form.errors) 
    return render(request, 'registration/login.html', {'form': form})
        

def custom_logout(request):
    logout(request)
    return redirect('/')  # Redirect to the login page after logout

def UpdateProfileView(r):
    # id = r.session.user_id
    user_id = r.session.get('user_id')
    obj = AuthUser.objects.get(id=user_id)
    return render(r,"pages/profile.html",{'obj':obj})

def UpdateProfile(r):
    if r.method=='POST':
        id = r.POST['id']
        obj = AuthUser.objects.get(id=id)
        
        name = r.POST.get('username')
        email = r.POST.get('email')
        
        obj.name = name
        obj.email = email
        obj.save()
        
        return HttpResponseRedirect("/updateprofileview/")
    return HttpResponseRedirect("/updateprofileview/")
 

# def UpdateProfile(r):
#     if r.method == 'POST':
#         id = r.POST.get('id')  # Use get() instead of indexing
#         obj = AuthUser.objects.get(id=id)
        
#         form = CustomUserLoginForm(r.POST, instance=obj)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect("updateprofileview/")  # Correct the URL
        
#     return render(r, "pages/profile.html", {'obj': obj})


# @login_required
# def change_password(request):
#     if request.method == 'POST':
#         form = PasswordChangeForm(request.user, request.POST)
#         if form.is_valid():
#             old_password = form.cleaned_data['old_password']
#             new_password1 = form.cleaned_data['new_password1']
#             new_password2 = form.cleaned_data['new_password2']
            
#             if old_password == new_password1:
#                 form.add_error('new_password1', "New password must be different from old password.")
#             elif new_password1 != new_password2:
#                 form.add_error('new_password2', "New passwords do not match.")
#             else:
#                 user = form.save()
#                 update_session_auth_hash(request, user)
#                 messages.success(request, 'Your password was successfully changed!')
#                 return redirect('profile')
#     else:
#         form = PasswordChangeForm(request.user)
    
#     return render(request, 'change_password.html', {'form': form})

@login_required
def ChangePassword(r):
    if r.method =='POST':
        id = r.POST['pass_id']
        obj = AuthUser.objects.get(id=id)
        if obj is not None:
            current_password = r.POST.get('current_password')
            new_password = r.POST.get('new_password')
            confirm_password = r.POST.get('confirm_password')
            
            if current_password == new_password:
                messages.error(r, "New password must be different from current password.")
            elif new_password != confirm_password:
                messages.error(r, "New passwords do not match.")               
            else:
                hashed_password = make_password(new_password)
                obj.password = hashed_password
                obj.save()
                messages.success(r, 'Your password was successfully changed!')
    return HttpResponseRedirect("/updateprofileview/")

def CompanyProfileView(r):
    # id = r.session.user_id
    obj = CompanyProfileModel.objects.get()

    return render(r,"registration/companyprofile.html",{'obj':obj})

def UpdateCompanyProfile(r):
    if r.method=='POST':
        
        id = r.POST['c_id']
        company_name = r.POST.get('company_name')
        website = r.POST.get('company_website')
        company_email = r.POST.get('company_email')
        account_email = r.POST.get('accounts_email')
        address = r.POST.get('address')
        city = r.POST.get('city')
        state = r.POST.get('state')
        pincode = r.POST.get('pincode')
        pan_number = r.POST.get('pan_number') 
        gst_number = r.POST.get('gst_number')
        iec_code = r.POST.get('iec_code')
        iso_certificate_number = r.POST.get('iso_certificate_number')
        primary_mobile = r.POST.get('primary_mobile')
        alternate_mobile = r.POST.get('alternate_mobile')
        account_name = r.POST.get('account_name')
        account_number = r.POST.get('account_number')
        bank_name = r.POST.get('bank_name')
        ifsc_code = r.POST.get('ifsc_code')
        
        obj = CompanyProfileModel.objects.get(id=id)
        
        obj.company_name = company_name
        obj.website = website
        obj.company_email = company_email
        obj.account_email = account_email
        obj.address = address
        obj.city = city
        obj.state = state
        obj.pincode = pincode
        obj.pan_number = pan_number
        obj.gst_number = gst_number
        obj.iec_code = iec_code
        obj.iso_certificate_number = iso_certificate_number
        obj.primary_mobile = primary_mobile
        obj.alternate_mobile = alternate_mobile
        obj.account_name = account_name
        obj.account_number = account_number
        obj.bank_name = bank_name
        obj.ifsc_code = ifsc_code

        
        # Move the uploaded files to the media directory
        if 'pan_file' in r.FILES:
            obj.pan_file = r.FILES['pan_file']
            
        if 'gst_file' in r.FILES:
            obj.gst_file = r.FILES['gst_file']
            
        if 'logo' in r.FILES:
            obj.logo_file = r.FILES['logo']
                
        if 'iso_file' in r.FILES:
            obj.iso_file = r.FILES['iso_file']
                
        obj.save()
   
    return HttpResponseRedirect("/companyprofile/")
 

 
    




