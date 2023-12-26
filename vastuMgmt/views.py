from django.shortcuts import render
from clientMgmt.models import ClientDetails
from .models import EtarUpay,VishesUpay,TwoD_ThreeD_Upay,VishesSalla,ExtraUpay,BSNUpay,Vastu,Disha,BadalDisha,Parinam,VastuMgmt
from django.contrib import messages 
from django.http import HttpResponseRedirect,JsonResponse,HttpResponse
from django.db.models import F, OuterRef, Subquery


# Create your views here.

def vastuMgmtView(r):
    client_list = ClientDetails.objects.filter(delete=0)
    vastu_list = Vastu.objects.filter(delete=0)
    disha_list = Disha.objects.filter(delete=0)
    badal_disha_list = BadalDisha.objects.filter(delete=0)
    bsnUpay_list = BSNUpay.objects.filter(delete=0)
    etar_upay_list = EtarUpay.objects.filter(delete=0)
    vis_upay_list = VishesUpay.objects.filter(delete=0)
    twoD_threeD_Upay_List = TwoD_ThreeD_Upay.objects.filter(delete=0)
    ext_upay_list = ExtraUpay.objects.filter(delete=0)
    vis_salla_list = VishesSalla.objects.filter(delete=0)
    
    return render(r, 'vastumgmt/vastumgmt.html',{'client_list':client_list,'vastu_list':vastu_list,'disha_list':disha_list,'badal_disha_list':badal_disha_list,'bsnUpay_list':bsnUpay_list,'etar_upay_list':etar_upay_list,'vis_upay_list':vis_upay_list,'twoD_threeD_Upay_List':twoD_threeD_Upay_List,'ext_upay_list':ext_upay_list,'vis_salla_list':vis_salla_list})

def getParinam(r):
    disha = r.GET.get('disha') 
    vastu = r.GET.get('vastu')      # get question id from question list in jyo_questions 
    parinam_list = Parinam.objects.filter(delete=0,vastu_id = vastu, disha_id=disha).values('id','vastu_id','disha_id', 'parinam')
    
    return JsonResponse({'parinam_list': list(parinam_list)})

def postVastuRecord(r):
    user_id = r.session.get('user_id')
    edit_id = r.POST.get('edit_id')
    client_name = r.POST.get('client_name')
    date_field = r.POST.get('date_field')
    vastu = r.POST.get('vastu')
    disha = r.POST.get('disha')
    parinam = r.POST.get('parinam')
    parinam_summernote = r.POST.get('parinam_summernote')
    badal_disha = r.POST.get('badal_disha')  
    bsn_upay = r.POST.get('bsn_upay')
    bsn_upay_summernote = r.POST.get('bsn_upay_summernote')
    
    
    etar_upay = r.POST.get('etar_upay')
    etar_upay_summernote = r.POST.get('etar_upay_summernote')
    vis_upay = r.POST.get('vis_upay')
    vis_upay_summernote = r.POST.get('vis_upay_summernote')
    twod_threed_upay = r.POST.get('twod_threed_upay')
    twoD_3D_upay_summernote = r.POST.get('twoD_3D_upay_summernote')
    ext_upay = r.POST.get('ext_upay')
    ext_upay_summernote = r.POST.get('ext_upay_summernote')
    vis_salla = r.POST.get('vis_salla')
    vis_salla_summernote = r.POST.get('vis_salla_summernote')
    #return JsonResponse({'status': True,'edit_id': edit_id,'client_name': client_name, 'vastu': vastu,'date_field': date_field,'disha': disha,'parinam':parinam,'parinam_summernote': parinam_summernote,'badal_disha' : badal_disha,'bsn_upay':bsn_upay,'bsn_upay_summernote':bsn_upay_summernote})
    if edit_id:
        
        #This is for Update Vastu Records
        obj = VastuMgmt.objects.get(id=edit_id)        
        obj.client_id=client_name
        obj.date_field=date_field
        obj.vastu_id=vastu
        obj.disha_id=disha
        obj.parinam_id=parinam
        obj.parinam=parinam_summernote
        obj.badal_disha_id=badal_disha
        obj.bsn_uday_id=bsn_upay
        obj.bsn_upay=bsn_upay_summernote
        obj.etar_upay_id=etar_upay
        obj.etar_upay=etar_upay_summernote
        obj.vis_upay_id=vis_upay
        obj.vis_upay=vis_upay_summernote
        obj.twod_threed_upay_id=twod_threed_upay
        obj.twod_threed_upay=twoD_3D_upay_summernote
        obj.ext_upay_id=ext_upay
        obj.ext_upay=ext_upay_summernote
        obj.vis_salla_id=vis_salla
        obj.vis_salla=vis_salla_summernote
        obj.save()
        
        #if jyo_questions is created successfully then if block will be executed
        if obj:
            return JsonResponse({'status': True,'message': 'Record Updated successfully'})
        
        else:
        #if jyo_questions is not created successfully then else block will be executed
            return JsonResponse({'status': False,'message': 'Record Updated Unsuccessfully'})
    else:
            
            #This is for Create Jyotishi Mgmt
            obj = VastuMgmt(
                client_id=client_name,
                date_field=date_field,
                vastu_id=vastu,
                disha_id=disha,
                parinam_id=parinam,
                parinam=parinam_summernote,
                badal_disha_id=badal_disha,
                bsn_upay_id=bsn_upay,
                bsn_upay=bsn_upay_summernote,
                etar_upay_id=etar_upay,
                etar_upay=etar_upay_summernote,
                vis_upay_id=vis_upay,
                vis_upay=vis_upay_summernote,
                twod_threed_upay_id=twod_threed_upay,
                twod_threed_upay=twoD_3D_upay_summernote,
                ext_upay_id=ext_upay,
                ext_upay=ext_upay_summernote,
                vis_salla_id=vis_salla,
                vis_salla=vis_salla_summernote,
                delete=0,
                a_id=user_id
            )
            obj.save()
            #if jyo_questions is created successfully then if block will be executed
            if obj:
                return JsonResponse({'status': True,'message': 'Record Added successfully'})
            
            else:
            #if jyo_questions is not created successfully then else block will be executed
                return JsonResponse({'status': False,'message': 'Record Added Unsuccessfully'})
                
def getVastuRecords(r):
    vastu_mgmt_list = VastuMgmt.objects.filter(delete=0).annotate(
                client_name=Subquery(
                    ClientDetails.objects.filter(id=OuterRef('client_id')).values('client_name')[:1]
                )
            ).annotate(
            vastu=Subquery(
                Vastu.objects.filter(id=OuterRef('vastu_id')).values('vastu')[:1]
            )
        ).annotate(
            disha=Subquery(
                Disha.objects.filter(id=OuterRef('disha_id')).values('disha')[:1]
            )
        ).annotate(
            badal_disha=Subquery(
                BadalDisha.objects.filter(id=OuterRef('badal_disha_id')).values('badal_disha')[:1]
            )
        ).values('id','client_id','client_name','date_field','vastu_id','vastu','disha_id','disha','parinam_id','parinam','badal_disha_id','badal_disha','bsn_upay_id','bsn_upay','etar_upay_id','etar_upay','vis_upay_id','vis_upay','twod_threed_upay_id','twod_threed_upay','ext_upay_id','ext_upay','vis_salla_id','vis_salla')
        
    return JsonResponse({'vastu_mgmt_list': list(vastu_mgmt_list)})

def vastuMgmtDelete(r,id):
    obj = VastuMgmt.objects.get(id=id)
    obj.delete = 1
    obj.save()
    messages.success(r, 'Vastu Management Deleted Successfully.')
    #Redirect to Vastu Question List   
    return HttpResponseRedirect("/vastumgmt/vastu_mgmt_view/")  

import pdfkit
from django.template.loader import render_to_string

def dowloadVastuPDF(r,id):
    
    data = VastuMgmt.objects.filter(delete=0,id=id).annotate(
                client_name=Subquery(
                    ClientDetails.objects.filter(id=OuterRef('client_id')).values('client_name')[:1]
                )
            ).annotate(
            vastu=Subquery(
                Vastu.objects.filter(id=OuterRef('vastu_id')).values('vastu')[:1]
            )
        ).annotate(
            disha=Subquery(
                Disha.objects.filter(id=OuterRef('disha_id')).values('disha')[:1]
            )
        ).annotate(
            badal_disha=Subquery(
                BadalDisha.objects.filter(id=OuterRef('badal_disha_id')).values('badal_disha')[:1]
            )
        ).values('id','client_id','client_name','date_field','vastu_id','vastu','disha_id','disha','parinam_id','parinam','badal_disha_id','badal_disha','bsn_upay_id','bsn_upay','etar_upay_id','etar_upay','vis_upay_id','vis_upay','twod_threed_upay_id','twod_threed_upay','ext_upay_id','ext_upay','vis_salla_id','vis_salla')
        
    queryset_dict = list(data)
    
    context = {
        'heading': queryset_dict,
        # Add more context variables as needed
    }

    # Render the HTML template with the context
    # html_content = render_to_string('pdfTemplate/your_template.html', context)
    html_content = render_to_string('vastumgmt/vastuPDF.html', context)
    
    

    # Configure options as needed
    options = {
        'page-size': 'A5',
        'encoding': 'UTF-8',
        # Include more options as per your requirements
    }

    # Generate PDF from HTML content
    pdf = pdfkit.from_string(html_content, False, options=options)

    # Prepare HTTP response with PDF content as attachment
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Vastu.pdf"'

    return response
    
    # print(jyo_mgmt_list)
    # # Your data and logic to generate HTML
    # context = {'content': smart_str('यह हिंदी में कुछ पाठ है।')}

    # # Render the HTML using a Django template
    # template_path = 'pdfTemplate/your_template.html'
    # template = render(r, template_path, context)

    # # Create PDF
    # pdf_data = BytesIO()
    # pdf = pisa.CreatePDF(template.content, dest=pdf_data)
    # if not pdf.err:
    #     return HttpResponse(pdf_data.getvalue(), content_type='application/pdf')

    # return HttpResponse('Error creating PDF: {}'.format(pdf.err))

    # # Get SummerNote content from the request or your model
    # summer_note_content = "Your SummerNote content here"

    # # Render HTML template with SummerNote content
    # html_content = render(r, 'billPDF.html', {'summer_note_content': summer_note_content})

    # # Generate PDF using WeasyPrint
    # pdf = HTML(string=html_content.content.decode('utf-8')).write_pdf()

    # # Create a Django response with the PDF content
    # response = HttpResponse(pdf, content_type='application/pdf')
    # response['Content-Disposition'] = 'filename="output.pdf"'
    
    
    
###################################### Start Etar Upay Master ######################################

def etarUpayView(r):
    etar_upay_list = EtarUpay.objects.filter(delete=0)
    return render(r, 'vastumgmt/etarupay.html',{'etar_upay_list':etar_upay_list })

def postEtarUpay(r):
    user_id = r.session.get('user_id')
    
    if r.method=='POST':
        edit_id = r.POST['edit_id']
        etar_upay = r.POST['etar_upay']

        if edit_id:
            #This is for Update Jyotishi Question
            obj = EtarUpay.objects.get(id=edit_id)
            obj.etar_upay = etar_upay
            obj.save()
            
            messages.success(r, 'Etar Upay Updated Successfully.')
        else:
            #This is for Create Jyotishi Question
            obj = EtarUpay(
                etar_upay=etar_upay,
                delete=0,
                a_id=user_id
            )
            obj.save()
            #if jyo_upay is created successfully then if block will be executed
            if obj:
                messages.success(r, 'Etar Upay Added Successfully.')
            
            else:
            #if jyo_upay is not created successfully then else block will be executed
                messages.error(r, 'Etar Upay Added UnSuccessfully.')
                
    #Redirect to Jyotishi Question List     
    return HttpResponseRedirect("/vastumgmt/etar_upay/")

def etarUpayDelete(r,id):
    obj = EtarUpay.objects.get(id=id)
    obj.delete = 1
    obj.save()
    messages.success(r, 'Etar Upay Deleted Successfully.')
    #Redirect to Jyotishi Question List   
    return HttpResponseRedirect("/vastumgmt/etar_upay/")

###################################### End Etar Upay Master #######################################

###################################### Start Vishes Upay Master ######################################

def vishesUpayView(r):
    vishes_upay_list = VishesUpay.objects.filter(delete=0)
    return render(r, 'vastumgmt/vishesupay.html',{'vishes_upay_list':vishes_upay_list })

def postVisUpay(r):
    user_id = r.session.get('user_id')
    
    if r.method=='POST':
        edit_id = r.POST['edit_id']
        vis_upay = r.POST['vis_upay']

        if edit_id:
            #This is for Update Jyotishi Question
            obj = VishesUpay.objects.get(id=edit_id)
            obj.vis_upay = vis_upay
            obj.save()
            
            messages.success(r, 'Vishes Upay Updated Successfully.')
        else:
            #This is for Create Jyotishi Question
            obj = VishesUpay(
                vis_upay=vis_upay,
                delete=0,
                a_id=user_id
            )
            obj.save()
            #if jyo_upay is created successfully then if block will be executed
            if obj:
                messages.success(r, 'Vishes Upay Added Successfully.')
            
            else:
            #if jyo_upay is not created successfully then else block will be executed
                messages.error(r, 'Vishes Upay Added UnSuccessfully.')
                
    #Redirect to Jyotishi Question List     
    return HttpResponseRedirect("/vastumgmt/vishes_upay/")

def visUpayDelete(r,id):
    obj = VishesUpay.objects.get(id=id)
    obj.delete = 1
    obj.save()
    messages.success(r, 'Vishes Upay Deleted Successfully.')
    #Redirect to Jyotishi Question List   
    return HttpResponseRedirect("/vastumgmt/vishes_upay/")

###################################### End Vishes Upay Master #######################################

###################################### Start 2D 3D Upay Master ######################################

def twoDthreeDUpayView(r):
    twod_threed_upay_list = TwoD_ThreeD_Upay.objects.filter(delete=0)
    return render(r, 'vastumgmt/2D_3D_upay.html',{'twod_threed_upay_list':twod_threed_upay_list })

def posttwoDthreeDUpay(r):
    user_id = r.session.get('user_id')
    
    if r.method=='POST':
        edit_id = r.POST['edit_id']
        twod_threed_upay = r.POST['twod_threed_upay']

        if edit_id:
            #This is for Update Jyotishi Question
            obj = TwoD_ThreeD_Upay.objects.get(id=edit_id)
            obj.twod_threed_upay = twod_threed_upay
            obj.save()
            
            messages.success(r, '2D 3D Upay Updated Successfully.')
        else:
            #This is for Create Jyotishi Question
            obj = TwoD_ThreeD_Upay(
                twod_threed_upay=twod_threed_upay,
                delete=0,
                a_id=user_id
            )
            obj.save()
            #if jyo_upay is created successfully then if block will be executed
            if obj:
                messages.success(r, '2D 3D Upay Added Successfully.')
            
            else:
            #if jyo_upay is not created successfully then else block will be executed
                messages.error(r, '2D 3D Upay Added UnSuccessfully.')
                
    #Redirect to Jyotishi Question List     
    return HttpResponseRedirect("/vastumgmt/twod_threed_upay/")

def twoDthreeDUpayDelete(r,id):
    obj = TwoD_ThreeD_Upay.objects.get(id=id)
    obj.delete = 1
    obj.save()
    messages.success(r, '2D 3D Upay Deleted Successfully.')
    #Redirect to Jyotishi Question List   
    return HttpResponseRedirect("/vastumgmt/twod_threed_upay/")

###################################### End 2D 3D Upay Master #######################################

###################################### Start Vishes Salla Master ######################################

def vishesSallaView(r):
    vishes_salla_list = VishesSalla.objects.filter(delete=0)
    return render(r, 'vastumgmt/vishessalla.html',{'vishes_salla_list':vishes_salla_list })

def postVisSalla(r):
    user_id = r.session.get('user_id')
    
    if r.method=='POST':
        edit_id = r.POST['edit_id']
        vis_salla = r.POST['vis_salla']

        if edit_id:
            #This is for Update Jyotishi Question
            obj = VishesSalla.objects.get(id=edit_id)
            obj.vis_salla = vis_salla
            obj.save()
            
            messages.success(r, 'Vishes Salla Updated Successfully.')
        else:
            #This is for Create Jyotishi Question
            obj = VishesSalla(
                vis_salla=vis_salla,
                delete=0,
                a_id=user_id
            )
            obj.save()
            #if jyo_upay is created successfully then if block will be executed
            if obj:
                messages.success(r, 'Vishes Salla Added Successfully.')
            
            else:
            #if jyo_upay is not created successfully then else block will be executed
                messages.error(r, 'Vishes Salla Added UnSuccessfully.')
                
    #Redirect to Jyotishi Question List     
    return HttpResponseRedirect("/vastumgmt/vishes_salla/")

def visSallaDelete(r,id):
    obj = VishesSalla.objects.get(id=id)
    obj.delete = 1
    obj.save()
    messages.success(r, 'Vishes Salla Deleted Successfully.')
    #Redirect to Jyotishi Question List   
    return HttpResponseRedirect("/vastumgmt/vishes_salla/")

###################################### End Vishes Salla Master #######################################

###################################### Start Extra Upay Master ######################################

def extraUpayView(r):
    extra_upay_list = ExtraUpay.objects.filter(delete=0)
    return render(r, 'vastumgmt/extraupay.html',{'extra_upay_list':extra_upay_list })

def postExtUpay(r):
    user_id = r.session.get('user_id')
    
    if r.method=='POST':
        edit_id = r.POST['edit_id']
        ext_upay = r.POST['ext_upay']

        if edit_id:
            #This is for Update Jyotishi Question
            obj = ExtraUpay.objects.get(id=edit_id)
            obj.ext_upay = ext_upay
            obj.save()
            
            messages.success(r, 'Extra Upay Updated Successfully.')
        else:
            #This is for Create Jyotishi Question
            obj = ExtraUpay(
                ext_upay=ext_upay,
                delete=0,
                a_id=user_id
            )
            obj.save()
            #if jyo_upay is created successfully then if block will be executed
            if obj:
                messages.success(r, 'Extra Upay Added Successfully.')
            
            else:
            #if jyo_upay is not created successfully then else block will be executed
                messages.error(r, 'Extra Upay Added UnSuccessfully.')
                
    #Redirect to Jyotishi Question List     
    return HttpResponseRedirect("/vastumgmt/extra_upay/")

def extUpayDelete(r,id):
    obj = ExtraUpay.objects.get(id=id)
    obj.delete = 1
    obj.save()
    messages.success(r, 'Extra Upay Deleted Successfully.')
    #Redirect to Jyotishi Question List   
    return HttpResponseRedirect("/vastumgmt/extra_upay/")

###################################### End Extra Upay Master #######################################

###################################### Start Badal Shakya Naslyas Upay Master ######################################

def bsnUpayView(r):
    bsn_upay_list = BSNUpay.objects.filter(delete=0)
    return render(r, 'vastumgmt/badal_sha_nas_upay.html',{'bsn_upay_list':bsn_upay_list })

def postBsnUpay(r):
    user_id = r.session.get('user_id')
    
    if r.method=='POST':
        edit_id = r.POST['edit_id']
        bsn_upay = r.POST['bsn_upay']

        if edit_id:
            #This is for Update Jyotishi Question
            obj = BSNUpay.objects.get(id=edit_id)
            obj.bsn_upay = bsn_upay
            obj.save()
            
            messages.success(r, 'BSN Upay Updated Successfully.')
        else:
            #This is for Create Jyotishi Question
            obj = BSNUpay(
                bsn_upay=bsn_upay,
                delete=0,
                a_id=user_id
            )
            obj.save()
            #if jyo_upay is created successfully then if block will be executed
            if obj:
                messages.success(r, 'BSN Upay Added Successfully.')
            
            else:
            #if jyo_upay is not created successfully then else block will be executed
                messages.error(r, 'BSN Upay Added UnSuccessfully.')
                
    #Redirect to Jyotishi Question List     
    return HttpResponseRedirect("/vastumgmt/bsn_upay/")

def bsnUpayDelete(r,id):
    obj = BSNUpay.objects.get(id=id)
    obj.delete = 1
    obj.save()
    messages.success(r, 'BSN Upay Deleted Successfully.')
    #Redirect to Jyotishi Question List   
    return HttpResponseRedirect("/vastumgmt/bsn_upay/")

###################################### End Badal Shakya Naslyas Upay Master #######################################

###################################### Start Vastu Master ######################################

def vastuView(r):
    vastu_list = Vastu.objects.filter(delete=0)
    return render(r, 'vastumgmt/vastu.html',{'vastu_list':vastu_list })

def postVastu(r):
    user_id = r.session.get('user_id')
    
    if r.method=='POST':
        edit_id = r.POST['edit_id']
        vastu = r.POST['vastu']

        if edit_id:
            #This is for Update Jyotishi Question
            obj = Vastu.objects.get(id=edit_id)
            obj.vastu = vastu
            obj.save()
            
            messages.success(r, 'Vastu Updated Successfully.')
        else:
            #This is for Create Jyotishi Question
            obj = Vastu(
                vastu=vastu,
                delete=0,
                a_id=user_id
            )
            obj.save()
            #if jyo_upay is created successfully then if block will be executed
            if obj:
                messages.success(r, 'Vastu Added Successfully.')
            
            else:
            #if jyo_upay is not created successfully then else block will be executed
                messages.error(r, 'Vastu Added UnSuccessfully.')
                
    #Redirect to Jyotishi Question List     
    return HttpResponseRedirect("/vastumgmt/vastu_view/")

def vastuDelete(r,id):
    obj = Vastu.objects.get(id=id)
    obj.delete = 1
    obj.save()
    messages.success(r, 'Vastu Deleted Successfully.')
    #Redirect to Jyotishi Question List   
    return HttpResponseRedirect("/vastumgmt/vastu_view/")

###################################### End Vastu Master #######################################

###################################### Start Disha Master ######################################

def dishaView(r):
    disha_list = Disha.objects.filter(delete=0)
    return render(r, 'vastumgmt/disha.html',{'disha_list':disha_list })

def postDisha(r):
    user_id = r.session.get('user_id')
    
    if r.method=='POST':
        edit_id = r.POST['edit_id']
        disha = r.POST['disha']

        if edit_id:
            #This is for Update Jyotishi Question
            obj = Disha.objects.get(id=edit_id)
            obj.disha = disha
            obj.save()
            
            messages.success(r, 'Disha Updated Successfully.')
        else:
            #This is for Create Jyotishi Question
            obj = Disha(
                disha=disha,
                delete=0,
                a_id=user_id
            )
            obj.save()
            #if jyo_upay is created successfully then if block will be executed
            if obj:
                messages.success(r, 'Disha Added Successfully.')
            
            else:
            #if jyo_upay is not created successfully then else block will be executed
                messages.error(r, 'Disha Added UnSuccessfully.')
                
    #Redirect to Jyotishi Question List     
    return HttpResponseRedirect("/vastumgmt/disha_view/")

def dishaDelete(r,id):
    obj = Disha.objects.get(id=id)
    obj.delete = 1
    obj.save()
    messages.success(r, 'Disha Deleted Successfully.')
    #Redirect to Jyotishi Question List   
    return HttpResponseRedirect("/vastumgmt/disha_view/")

###################################### End Disha Master #######################################

###################################### Start Badal Disha Master ######################################

def badalDishaView(r):
    badal_disha_list = BadalDisha.objects.filter(delete=0)
    return render(r, 'vastumgmt/badaldisha.html',{'badal_disha_list':badal_disha_list })

def postBadalDisha(r):
    user_id = r.session.get('user_id')
    
    if r.method=='POST':
        edit_id = r.POST['edit_id']
        badal_disha = r.POST['badal_disha']

        if edit_id:
            #This is for Update Jyotishi Question
            obj = BadalDisha.objects.get(id=edit_id)
            obj.badal_disha = badal_disha
            obj.save()
            
            messages.success(r, 'Badal Disha Updated Successfully.')
        else:
            #This is for Create Jyotishi Question
            obj = BadalDisha(
                badal_disha=badal_disha,
                delete=0,
                a_id=user_id
            )
            obj.save()
            #if jyo_upay is created successfully then if block will be executed
            if obj:
                messages.success(r, 'Badal Disha Added Successfully.')
            
            else:
            #if jyo_upay is not created successfully then else block will be executed
                messages.error(r, 'Badal Disha Added UnSuccessfully.')
                
    #Redirect to Jyotishi Question List     
    return HttpResponseRedirect("/vastumgmt/badaldisha_view/")

def badalDishaDelete(r,id):
    obj = BadalDisha.objects.get(id=id)
    obj.delete = 1
    obj.save()
    messages.success(r, 'Badal Disha Deleted Successfully.')
    #Redirect to Jyotishi Question List   
    return HttpResponseRedirect("/vastumgmt/badaldisha_view/")

###################################### End Badal Disha Master #######################################

###################################### Start Parinam Master ######################################

def parinamView(r):
    vastu_list = Vastu.objects.filter(delete=0)
    disha_list = Disha.objects.filter(delete=0)
    
    
    parinam_list = Parinam.objects.filter(delete=0).annotate(
    vastu=Subquery(
        Vastu.objects.filter(id=OuterRef('vastu_id')).values('vastu')[:1]
    )
).annotate(
    disha=Subquery(
        Disha.objects.filter(id=OuterRef('disha_id')).values('disha')[:1]
    )
).values('id','vastu_id','disha_id','vastu','disha','parinam')


    return render(r, 'vastumgmt/parinam.html',{'vastu_list':vastu_list, 'disha_list':disha_list, 'parinam_list':parinam_list})

def postParinam(r):
    user_id = r.session.get('user_id')
    
    if r.method=='POST':
        edit_id = r.POST['edit_id']
        parinam = r.POST['parinam']   
        vastu = r.POST['vastu']
        disha = r.POST['disha']
        
    
        if edit_id:
            #This is for Update Jyotishi Question
            obj = Parinam.objects.get(id=edit_id)
            obj.parinam = parinam
            obj.vastu_id = vastu
            obj.disha_id = disha
            obj.save()
            
            messages.success(r, 'Parinam Updated Successfully.')
        else:
            #This is for Create Jyotishi Question
            obj = Parinam(
                parinam=parinam,
                vastu_id = vastu,
                disha_id = disha,
                delete=0,
                a_id=user_id)
            obj.save()
            #if jyo_salla is created successfully then if block will be executed
            if obj:
                messages.success(r, 'Parinam Added Successfully.')
            else:
            #if jyo_salla is not created successfully then else block will be executed
                messages.error(r, 'Parinam Added UnSuccessfully.')
    #Redirect to Jyotishi Question List     
    return HttpResponseRedirect("/vastumgmt/parinam_view/")

def parinamDelete(r,id):
    obj = Parinam.objects.get(id=id)
    obj.delete = 1
    obj.save()
    messages.success(r, 'Parinam Deleted Successfully.')
    #Redirect to Jyotishi Question List   
    return HttpResponseRedirect("/vastumgmt/parinam_view/")

###################################### End parinam Master #######################################



