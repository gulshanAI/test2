from django.shortcuts import render
from clientMgmt.models import ClientDetails
from .models import JyotishiQuestions,JyotishiUpay,JyotishiSalla,VishesSalla,KarmikUpay,JyotishiMgmt
from django.contrib import messages 
from django.http import HttpResponseRedirect,JsonResponse,HttpResponse
from django.db.models import F, OuterRef, Subquery
from rest_framework.response import Response
from datetime import datetime
from babel.dates import format_date,Locale

# Create your views here.

def jyotishiView(r):
    # client_list = ClientDetails.objects.all()
    client_list = ClientDetails.objects.filter(delete=0)
    jyo_que_list = JyotishiQuestions.objects.filter(delete=0)
    jyo_upay_list = JyotishiUpay.objects.filter(delete=0)
    print(jyo_upay_list)
    return render(r, 'jyotishimgmt/jyotishimgmt.html',{'client_list':client_list, 'jyo_que_list':jyo_que_list, 'jyo_upay_list':jyo_upay_list})

def getJyoSalla(r):
    jyo_questions = r.GET.get('jyo_questions')      # get question id from question list in jyo_questions 
    
    jyo_salla_list = JyotishiSalla.objects.filter(delete=0,jyoque_id=jyo_questions).values('id','jyoque_id', 'jyo_salla')
    vis_salla_list = VishesSalla.objects.filter(delete=0,jyoque_id=jyo_questions).values('id','jyoque_id', 'vis_salla')
    kar_upay_list = KarmikUpay.objects.filter(delete=0,jyoque_id=jyo_questions).values('id','jyoque_id', 'kar_upay')
    
    return JsonResponse({'jyo_salla_list': list(jyo_salla_list),'vis_salla_list': list(vis_salla_list),'kar_upay_list': list(kar_upay_list)})

def postJyoRecord(r):
    user_id = r.session.get('user_id')
    # return JsonResponse({'status': True,'message': 'Record Updated successfully'})
    
    edit_id = r.POST.get('edit_id')
    client_name = r.POST.get('client_name')
    date = r.POST.get('date')
    jyo_que_summernote = r.POST.get('jyo_que_summernote')
    jyo_upay_summernote = r.POST.get('jyo_upay_summernote')
    jyo_salla_summernote = r.POST.get('jyo_salla_summernote')
    vis_salla_summernote = r.POST.get('vis_salla_summernote')
    kar_upay_summernote = r.POST.get('kar_upay_summernote')
    
    jyo_que_id = r.POST.get('jyo_questions')
    jyo_upay_id = r.POST.get('jyo_upay')
    jyo_salla_id = r.POST.get('jyo_salla')
    vis_salla_id = r.POST.get('vis_salla')
    kar_upay_id = r.POST.get('kar_upay')
    
    #return JsonResponse({'status': True,'message': 'Record Updated successfully','jyo_upay_id':jyo_upay_id,'kar_upay_id':kar_upay_id,'vis_salla_id':vis_salla_id,'jyo_salla_id':jyo_salla_id,'jyo_que_id':jyo_que_id,'jyo_salla_summernote':jyo_salla_summernote})
    
    if edit_id:
        #This is for Update Jyotishi Question
        obj = JyotishiMgmt.objects.get(id=edit_id)
        obj.client_id_id=client_name
        obj.date_field=date
        obj.jyo_questions=jyo_que_summernote
        obj.jyo_upay=jyo_upay_summernote
        obj.jyo_salla=jyo_salla_summernote
        obj.vis_salla=vis_salla_summernote
        obj.kar_upay=kar_upay_summernote
        obj.jyo_que_id=jyo_que_id
        obj.jyo_upay_id=jyo_upay_id
        obj.yo_salla_id=jyo_salla_id
        obj.vis_salla_id=vis_salla_id
        obj.kar_upay_id=kar_upay_id
        obj.save()
        
        #if jyo_questions is created successfully then if block will be executed
        if obj:
            return JsonResponse({'status': True,'message': 'Record Updated successfully'})
        
        else:
        #if jyo_questions is not created successfully then else block will be executed
            return JsonResponse({'status': False,'message': 'Record Updated Unsuccessfully'})
        
        
    else:
            #This is for Create Jyotishi Mgmt
            obj = JyotishiMgmt(
                client_id_id=client_name,
                date_field=date,
                jyo_questions=jyo_que_summernote,
                jyo_upay=jyo_upay_summernote,
                jyo_salla=jyo_salla_summernote,
                vis_salla=vis_salla_summernote,
                kar_upay=kar_upay_summernote,
                jyo_que_id=jyo_que_id,
                jyo_upay_id=jyo_upay_id,
                jyo_salla_id=jyo_salla_id,
                vis_salla_id=vis_salla_id,
                kar_upay_id=kar_upay_id,
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
                
def getJyoRecords(r):
    jyo_mgmt_list = JyotishiMgmt.objects.filter(delete=0).annotate(
        client_name=Subquery(
            ClientDetails.objects.filter(id=OuterRef('client_id_id')).values('client_name')[:1]
        )
    ).values('id','client_id_id','client_name','date_field','jyo_questions','jyo_upay','jyo_salla','vis_salla','kar_upay','jyo_que_id','jyo_upay_id','jyo_salla_id','vis_salla_id','kar_upay_id')
    
    return JsonResponse({'jyo_mgmt_list': list(jyo_mgmt_list)})
        
def jyoMgmtDelete(r,id):
    obj = JyotishiMgmt.objects.get(id=id)
    obj.delete = 1
    obj.save()
    messages.success(r, 'Jyotishi Management Deleted Successfully.')
    #Redirect to Jyotishi Question List   
    return HttpResponseRedirect("/jyotishimgmt/jyotishi_view/")    
 
import pdfkit
from django.template.loader import render_to_string

def dowloadJyotishiPDF(r,id):
    
    data = JyotishiMgmt.objects.filter(delete=0,id=id).annotate(
        client_name=Subquery(
            ClientDetails.objects.filter(id=OuterRef('client_id_id')).values('client_name')[:1]
        )
    ).values('id','client_id_id','client_name','date_field','jyo_questions','jyo_upay','jyo_salla','vis_salla','kar_upay','jyo_que_id','jyo_upay_id','jyo_salla_id','vis_salla_id','kar_upay_id')

    
    queryset_dict = list(data)
    
    context = {
        'heading': queryset_dict,
        # Add more context variables as needed
    }

    # Render the HTML template with the context
    # html_content = render_to_string('pdfTemplate/your_template.html', context)
    html_content = render_to_string('jyotishimgmt/jyotishiPDF.html', context)
    
    

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
    response['Content-Disposition'] = 'attachment; filename="Jyotishi.pdf"'

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
    
###################################### Start Jyotishi Questions Master ####################################

def jyotishiQuestionsView(r):
    jyo_que_list = JyotishiQuestions.objects.filter(delete=0)
    return render(r, 'jyotishimgmt/jyotishiquestions.html',{'jyo_que_list':jyo_que_list })

def postjyoQuestions(r):
    user_id = r.session.get('user_id')
    
    if r.method=='POST':
        edit_id = r.POST['edit_id']
        jyo_questions = r.POST['jyo_questions']

        if edit_id:
            #This is for Update Jyotishi Question
            obj = JyotishiQuestions.objects.get(id=edit_id)
            obj.jyo_questions = jyo_questions
            obj.save()
            
            messages.success(r, 'Question Updated Successfully.')
        else:
            #This is for Create Jyotishi Question
            obj = JyotishiQuestions(
                jyo_questions=jyo_questions,
                delete=0,
                a_id=user_id
            )
            obj.save()
            #if jyo_questions is created successfully then if block will be executed
            if obj:
                messages.success(r, 'Question Added Successfully.')
            
            else:
            #if jyo_questions is not created successfully then else block will be executed
                messages.error(r, 'Question Added UnSuccessfully.')
                
    #Redirect to Jyotishi Question List     
    return HttpResponseRedirect("/jyotishimgmt/jyotishi_que/")

def jyoQuestionDelete(r,id):
    obj = JyotishiQuestions.objects.get(id=id)
    obj.delete = 1
    obj.save()
    messages.success(r, 'Question Deleted Successfully.')
    #Redirect to Jyotishi Question List   
    return HttpResponseRedirect("/jyotishimgmt/jyotishi_que/")

###################################### End Jyotishi Questions Master ####################################

###################################### Start Jyotishi Upay Master ######################################

def jyotishiUpayView(r):
    jyo_upay_list = JyotishiUpay.objects.filter(delete=0)
    return render(r, 'jyotishimgmt/jyotishiupay.html',{'jyo_upay_list':jyo_upay_list })

def postjyoUpay(r):
    user_id = r.session.get('user_id')
    
    if r.method=='POST':
        edit_id = r.POST['edit_id']
        jyo_upay = r.POST['jyo_upay']

        if edit_id:
            #This is for Update Jyotishi Question
            obj = JyotishiUpay.objects.get(id=edit_id)
            obj.jyo_upay = jyo_upay
            obj.save()
            
            messages.success(r, 'Jyotishi Upay Updated Successfully.')
        else:
            #This is for Create Jyotishi Question
            obj = JyotishiUpay(
                jyo_upay=jyo_upay,
                delete=0,
                a_id=user_id
            )
            obj.save()
            #if jyo_upay is created successfully then if block will be executed
            if obj:
                messages.success(r, 'Jyotishi Upay Added Successfully.')
            
            else:
            #if jyo_upay is not created successfully then else block will be executed
                messages.error(r, 'Jyotishi Upay Added UnSuccessfully.')
                
    #Redirect to Jyotishi Question List     
    return HttpResponseRedirect("/jyotishimgmt/jyotishi_upay/")

def jyoUpayDelete(r,id):
    obj = JyotishiUpay.objects.get(id=id)
    obj.delete = 1
    obj.save()
    messages.success(r, 'Question Deleted Successfully.')
    #Redirect to Jyotishi Question List   
    return HttpResponseRedirect("/jyotishimgmt/jyotishi_upay/")

###################################### End Jyotishi Upay Master #######################################

###################################### Start Jyotishi Salla Master ######################################

def jyotishiSallaView(r):
    jyo_que_list = JyotishiQuestions.objects.filter(delete=0)
    
    jyo_salla_list = JyotishiSalla.objects.filter(delete=0).annotate(
        jyo_questions=Subquery(
            JyotishiQuestions.objects.filter(id=OuterRef('jyoque_id')).values('jyo_questions')[:1]
        )
    ).values('id','jyoque_id','jyo_questions', 'jyo_salla')
     
    return render(r, 'jyotishimgmt/jyotishisalla.html',{'jyo_salla_list':jyo_salla_list, 'jyo_que_list':jyo_que_list})

def postJyoSalla(r):
    user_id = r.session.get('user_id')
    
    if r.method=='POST':
        edit_id = r.POST['edit_id']
        jyo_salla = r.POST['jyo_salla']   
        jyo_questions = r.POST['jyo_questions']
        

        if edit_id:
            #This is for Update Jyotishi Question
            obj = JyotishiSalla.objects.get(id=edit_id)
            obj.jyo_salla = jyo_salla
            obj.jyoque_id = jyo_questions
            obj.save()
            
            messages.success(r, 'Jyotishi Salla Updated Successfully.')
        else:
            #This is for Create Jyotishi Question
            obj = JyotishiSalla(
                jyo_salla=jyo_salla,
                jyoque_id = jyo_questions,
                delete=0,
                a_id=user_id)
            obj.save()
            #if jyo_salla is created successfully then if block will be executed
            if obj:
                messages.success(r, 'Jyotishi Salla Added Successfully.')
            else:
            #if jyo_salla is not created successfully then else block will be executed
                messages.error(r, 'Jyotishi Salla Added UnSuccessfully.')
    #Redirect to Jyotishi Question List     
    return HttpResponseRedirect("/jyotishimgmt/jyotishi_salla/")

def jyoSallaDelete(r,id):
    obj = JyotishiSalla.objects.get(id=id)
    obj.delete = 1
    obj.save()
    messages.success(r, 'Jyotishi Salla Deleted Successfully.')
    #Redirect to Jyotishi Question List   
    return HttpResponseRedirect("/jyotishimgmt/jyotishi_salla/")

###################################### End Jyotishi Salla Master #######################################

###################################### Start Vishes Salla Master ######################################

def vishesSallaView(r):
    jyo_que_list = JyotishiQuestions.objects.filter(delete=0)
    
    vis_salla_list = VishesSalla.objects.filter(delete=0).annotate(
        jyo_questions=Subquery(
            JyotishiQuestions.objects.filter(id=OuterRef('jyoque_id')).values('jyo_questions')[:1]
        )
    ).values('id','jyoque_id','jyo_questions', 'vis_salla')
     
    return render(r, 'jyotishimgmt/vishessalla.html',{'vis_salla_list':vis_salla_list, 'jyo_que_list':jyo_que_list})

def postVisSalla(r):
    user_id = r.session.get('user_id')
    
    if r.method=='POST':
        edit_id = r.POST['edit_id']
        vis_salla = r.POST['vis_salla']   
        jyo_questions = r.POST['jyo_questions']
        

        if edit_id:
            #This is for Update Jyotishi Question
            obj = VishesSalla.objects.get(id=edit_id)
            obj.vis_salla = vis_salla
            obj.jyoque_id = jyo_questions
            obj.save()
            
            messages.success(r, 'Vishes Salla Updated Successfully.')
        else:
            #This is for Create Jyotishi Question
            obj = VishesSalla(
                vis_salla=vis_salla,
                jyoque_id = jyo_questions,
                delete=0,
                a_id=user_id)
            obj.save()
            #if jyo_salla is created successfully then if block will be executed
            if obj:
                messages.success(r, 'Vishes Salla Added Successfully.')
            else:
            #if jyo_salla is not created successfully then else block will be executed
                messages.error(r, 'Vishes Salla Added UnSuccessfully.')
    #Redirect to Jyotishi Question List     
    return HttpResponseRedirect("/jyotishimgmt/vishes_salla/")

def visSallaDelete(r,id):
    obj = VishesSalla.objects.get(id=id)
    obj.delete = 1
    obj.save()
    messages.success(r, 'Vishes Salla Deleted Successfully.')
    #Redirect to Jyotishi Question List   
    return HttpResponseRedirect("/jyotishimgmt/vishes_salla/")

###################################### End Vishes Salla Master #######################################

####################################### Start Karmik Salla Master ######################################

def karmicUpayView(r):
    jyo_que_list = JyotishiQuestions.objects.filter(delete=0)
    
    kar_upay_list = KarmikUpay.objects.filter(delete=0).annotate(
        jyo_questions=Subquery(
            JyotishiQuestions.objects.filter(id=OuterRef('jyoque_id')).values('jyo_questions')[:1]
        )
    ).values('id','jyoque_id','jyo_questions', 'kar_upay')
     
    return render(r, 'jyotishimgmt/karmikupay.html',{'kar_upay_list':kar_upay_list, 'jyo_que_list':jyo_que_list})

def postKarUpay(r):
    user_id = r.session.get('user_id')
    
    if r.method=='POST':
        edit_id = r.POST['edit_id']
        kar_upay = r.POST['kar_upay']   
        jyo_questions = r.POST['jyo_questions']
        

        if edit_id:
            #This is for Update Jyotishi Question
            obj = KarmikUpay.objects.get(id=edit_id)
            obj.kar_upay = kar_upay
            obj.jyoque_id = jyo_questions
            obj.save()
            
            messages.success(r, 'Karmic Upay Updated Successfully.')
        else:
            #This is for Create Jyotishi Question
            obj = KarmikUpay(
                kar_upay=kar_upay,
                jyoque_id = jyo_questions,
                delete=0,
                a_id=user_id)
            obj.save()
            #if jyo_salla is created successfully then if block will be executed
            if obj:
                messages.success(r, 'Karmic Upay Added Successfully.')
            else:
            #if jyo_salla is not created successfully then else block will be executed
                messages.error(r, 'Karmic Upay Added UnSuccessfully.')
    #Redirect to Jyotishi Question List     
    return HttpResponseRedirect("/jyotishimgmt/karmic_upay/")

def karUpayDelete(r,id):
    obj = KarmikUpay.objects.get(id=id)
    obj.delete = 1
    obj.save()
    messages.success(r, 'Karmic Upay Deleted Successfully.')
    #Redirect to Jyotishi Question List   
    return HttpResponseRedirect("/jyotishimgmt/karmic_upay/")

# ###################################### End Karmic Salla Master #######################################

