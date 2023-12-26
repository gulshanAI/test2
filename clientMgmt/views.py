from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import ClientDetails
from django.contrib import messages 

# Create your views here.

def clientView(r):
    # client_list = ClientDetails.objects.all()
    client_list = ClientDetails.objects.filter(delete=0)
    print(client_list)
    return render(r, 'clientmgmt/clientmgmt.html',{'client_list':client_list })

def postClient(r):
    user_id = r.session.get('user_id')
    
    if r.method=='POST':
        edit_id = r.POST['edit_id']
        client_name = r.POST['client_name']
        mobile = r.POST['mobile']

        if edit_id:
            obj = ClientDetails.objects.get(id=edit_id)
            obj.client_name = client_name
            obj.mobile = mobile
            obj.save()
            
            messages.success(r, 'Client updated successfully.')
        else:
            #This is for Create client
            obj = ClientDetails(
                client_name=client_name,
                mobile=mobile,
                delete=0,
                a_id=user_id
            )
            obj.save()
            
            if obj:
                messages.success(r, 'Client created Successfully.')
            else:
                messages.error(r, 'Client created UnSuccessfully.')
            
    return HttpResponseRedirect("/clientmgmt/client_view/")

def clientDelete(r,id):
    obj = ClientDetails.objects.get(id=id)
    obj.delete = 1
    obj.save()
    messages.success(r, 'Client deleted successfully.')
    
    return HttpResponseRedirect('/clientmgmt/client_view/')