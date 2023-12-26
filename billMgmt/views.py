from django.shortcuts import render
from .models import BillMgmt, BillItem
from stockMgmt.models import ProductType, ProductName, CompanyName
from clientMgmt.models import ClientDetails
from jyotishiMgmt.models import JyotishiMgmt
from django.contrib import messages 
from django.http import HttpResponseRedirect,JsonResponse,HttpResponse
from django.db.models import F, OuterRef, Subquery
from django.template.loader import get_template
from django.template import Context
#from weasyprint import HTML
# views.py
from django.shortcuts import render
from django.http import HttpResponse
from xhtml2pdf import pisa
from io import BytesIO
from django.utils.encoding import smart_str


# Create your views here.

def billView(r):
    client_list = ClientDetails.objects.filter(delete=0)
    pro_typ_list = ProductType.objects.filter(delete=0)
    if r.method=='POST':
        s_client_name = r.POST.get('s_client_name', '')
        s_product_type = r.POST.get('s_product_type', '') 
        s_product_name = r.POST.get('s_product_name', '')  # Use '' as the default value
        s_company_name = r.POST.get('s_company_name', '') # Use '' as the default value
        from_date = r.POST['from_date']
        to_date = r.POST['to_date']
        
        bill_list = BillMgmt.objects.filter(delete=0,date__range=[from_date, to_date]).annotate(
                client_name=Subquery(
                    ClientDetails.objects.filter(id=OuterRef('client_id')).values('client_name')[:1]
                )
            ).annotate(
                product_type=Subquery(
                    ProductType.objects.filter(id=OuterRef('protype_id')).values('product_type')[:1]
                )
            ).annotate(
            product_name=Subquery(
                ProductName.objects.filter(id=OuterRef('proname_id')).values('product_name')[:1]
            )
        ).annotate(
            company_name=Subquery(
                CompanyName.objects.filter(id=OuterRef('comname_id')).values('company_name')[:1]
            )
        ).values('id','client_id','client_name','protype_id','product_type','proname_id','product_name','comname_id','company_name','date','product_weight','product_units','product_quantity','sell_amount','total_amount','ret_validity','ret_percentage','ret_amount','exc_validity','exc_percentage','exc_amount')
        
        if s_client_name:
            bill_list = bill_list.filter(client_id=s_client_name)
            
        if s_product_type:
            bill_list = bill_list.filter(protype_id=s_product_type)
        
        if s_product_name:
            bill_list = bill_list.filter(proname_id=s_product_name)
            
        if s_company_name:
            bill_list = bill_list.filter(proname_id=s_company_name)
            
        for item in bill_list:
            item['date'] = item['date'].strftime('%Y-%m-%d')
        
        
    else:
        bill_list = BillMgmt.objects.filter(delete=0).annotate(
                client_name=Subquery(
                    ClientDetails.objects.filter(id=OuterRef('client_id')).values('client_name')[:1]
                )
            ).values('id','date','client_name')
        
        # for item in bill_list:
        #     item['date'] = item['date'].strftime('%Y-%m-%d')
            
    return render(r, 'billmgmt/billmgmt.html', {'client_list':client_list,'pro_typ_list':pro_typ_list, 'bill_list':bill_list})


def postBill(r):
    user_id = r.session.get('user_id')
    
    if r.method=='POST':
        client_name = r.POST['client_name']

        #This is for add bill client
        obj = BillMgmt(
            client_id = client_name,
            delete=0,
            a_id=user_id)
        obj.save()
        
        bill_id = obj.id
       
       
                
    #Redirect to customer add bill product page    
   
    return HttpResponseRedirect(f"/billmgmt/add_bill/{bill_id}")

def addBill(r,id):
    
    user_id = r.session.get('user_id')
    
    pro_typ_list = ProductType.objects.filter(delete=0)
    bill_id = id
    
    return render(r, 'billmgmt/bill_add.html', {'bill_id':bill_id,'pro_typ_list':pro_typ_list})
    
def postBillProduct(r):
    user_id = r.session.get('user_id')
    
    edit_id = r.POST['edit_id']
    bill_id = r.POST['bill_id']
    product_type = r.POST['product_type']
    product_name = r.POST['product_name']   
    company_name = r.POST['company_name']
    product_weight = r.POST['product_weight']
    product_units = r.POST['product_units']
    product_quantity = r.POST['product_quantity']
    sell_amount = r.POST['sell_amount']
    total_amount = r.POST['total_amount']
    ret_validity = r.POST['ret_validity']
    ret_percentage = r.POST['ret_percentage']
    ret_amount = r.POST['ret_amount']
    exc_validity = r.POST['exc_validity']
    exc_percentage = r.POST['exc_percentage']
    exc_amount = r.POST['exc_amount']
        
    if edit_id:
        
        #This is for Update Jyotishi Question
        obj = BillItem.objects.get(id=edit_id)
        obj.bill_id = bill_id
        obj.protype_id = product_type
        obj.proname_id = product_name
        obj.comname_id = company_name
        obj.product_weight = product_weight
        obj.product_units = product_units
        obj.product_quantity = product_quantity
        obj.sell_amount = sell_amount
        obj.total_amount = total_amount
        obj.ret_validity = ret_validity
        obj.ret_percentage = ret_percentage
        obj.ret_amount = ret_amount
        obj.exc_validity = exc_validity
        obj.exc_percentage = exc_percentage
        obj.exc_amount = exc_amount
        obj.save()
        
        #if Product is created successfully then if block will be executed
        if obj:
            return JsonResponse({'status': True,'message': 'Product Updated successfully'})
        
        else:
            #if Product is not created successfully then else block will be executed
            return JsonResponse({'status': False,'message': 'Product Updated Unsuccessfully'})
        
    else:
        
        #This is for Create Jyotishi Question
        obj = BillItem(
            bill_id = bill_id,
            protype_id = product_type,
            proname_id = product_name,
            comname_id = company_name,
            product_weight = product_weight,
            product_units = product_units,
            product_quantity = product_quantity,
            sell_amount = sell_amount,
            total_amount = total_amount,
            ret_validity = ret_validity,
            ret_percentage = ret_percentage,
            ret_amount = ret_amount,
            exc_validity = exc_validity,
            exc_percentage = exc_percentage,
            exc_amount = exc_amount,
            delete=0,
            a_id=user_id)
        obj.save()
        
        #if Product is created successfully then if block will be executed
        if obj:
            return JsonResponse({'status': True,'message': 'Product Added successfully'})
        
        else:
            #if Product is not created successfully then else block will be executed
            return JsonResponse({'status': False,'message': 'Product Added Unsuccessfully'})
            
def billMgmtDelete(r,id):
    obj = BillMgmt.objects.get(id=id)
    obj.delete = 1
    obj.save()
    messages.success(r, 'Bill Management Deleted Successfully.')
    #Redirect to Jyotishi Question List   
    return HttpResponseRedirect("/billmgmt/bill_view/")


def getBillRecords(r):
    bill_id = r.GET['bill_id']
    bill_list = BillItem.objects.filter(delete=0,bill_id=bill_id).annotate(
                product_type=Subquery(
                    ProductType.objects.filter(id=OuterRef('protype_id')).values('product_type')[:1]
                )
            ).annotate(
            product_name=Subquery(
                ProductName.objects.filter(id=OuterRef('proname_id')).values('product_name')[:1]
            )
        ).annotate(
            company_name=Subquery(
                CompanyName.objects.filter(id=OuterRef('comname_id')).values('company_name')[:1]
            )
        ).values('id','protype_id','product_type','proname_id','product_name','comname_id','company_name','product_weight','product_units','product_quantity','sell_amount','total_amount','ret_validity','ret_percentage','ret_amount','exc_validity','exc_percentage','exc_amount')
        
    return JsonResponse({'bill_list': list(bill_list)})

def billProductDelete(r):
    
    id = r.POST['prid']
    obj = BillItem.objects.get(id=id)
    obj.delete = 1
    obj.save()

    if obj:
        return JsonResponse({'status': True,'message': 'Product Deleted successfully'})
    else:
        #if Product is not deleted successfully then else block will be executed
        return JsonResponse({'status': False,'message': 'Product Deleted Unsuccessfully'})
    
def generateBill(r,id):
    user_id = r.session.get('user_id')
    if r.method=='POST':
        
        items_total = r.POST['items_total']
        date = r.POST['date']
        
        obj = BillMgmt.objects.get(id=id)
        obj.total_bill_amount = items_total
        obj.date = date
        obj.a_id = user_id
        obj.save()
        
        if obj:
            messages.success(r, 'Bill Generate Successfully.')
        else:
            messages.error(r, 'Bill Generated UnSuccessfully.')
    else:
        messages.error(r, 'Bill Generated UnSuccessfully.')
        
    return HttpResponseRedirect(f"/billmgmt/add_bill/{id}")


import pdfkit
from django.template.loader import render_to_string

def generateBillPDF(r,id):
    
    data = BillMgmt.objects.filter(delete=0,id=id).annotate(
                client_name=Subquery(
                    ClientDetails.objects.filter(id=OuterRef('client_id')).values('client_name')[:1]
                )
            ).values('id','client_id','date','client_name','total_bill_amount')
        
    bill_list = BillItem.objects.filter(delete=0,bill_id=id).annotate(
                product_type=Subquery(
                    ProductType.objects.filter(id=OuterRef('protype_id')).values('product_type')[:1]
                )
            ).annotate(
            product_name=Subquery(
                ProductName.objects.filter(id=OuterRef('proname_id')).values('product_name')[:1]
            )
        ).annotate(
            company_name=Subquery(
                CompanyName.objects.filter(id=OuterRef('comname_id')).values('company_name')[:1]
            )
        ).values('id','protype_id','product_type','proname_id','product_name','comname_id','company_name','product_weight','product_units','product_quantity','sell_amount','total_amount','ret_validity','ret_percentage','ret_amount','exc_validity','exc_percentage','exc_amount')
    
    for item in data:
        item['date'] = item['date'].strftime('%d-%m-%Y')
    
    queryset_dict = list(data)
    bill_list = list(bill_list)
    
    
    context = {
        'heading': queryset_dict,
        'bill_list': bill_list,
        # Add more context variables as needed
    }

    # Render the HTML template with the context
    # html_content = render_to_string('pdfTemplate/your_template.html', context)
    html_content = render_to_string('billmgmt/billPDF.html', context)
    
    

    # Configure options as needed
    options = {
        'page-size': 'A4',
        'encoding': 'UTF-8',
        # Include more options as per your requirements
    }

    # Generate PDF from HTML content
    pdf = pdfkit.from_string(html_content, False, options=options)

    # Prepare HTTP response with PDF content as attachment
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="hindi_content.pdf"'

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
    
    
    
def dowloadBillPDF(r,id):
    
    data = BillMgmt.objects.filter(delete=0,id=id).annotate(
                client_name=Subquery(
                    ClientDetails.objects.filter(id=OuterRef('client_id')).values('client_name')[:1]
                )
            ).values('id','client_id','client_name','total_bill_amount')
        
    bill_list = BillItem.objects.filter(delete=0,bill_id=id).annotate(
                product_type=Subquery(
                    ProductType.objects.filter(id=OuterRef('protype_id')).values('product_type')[:1]
                )
            ).annotate(
            product_name=Subquery(
                ProductName.objects.filter(id=OuterRef('proname_id')).values('product_name')[:1]
            )
        ).annotate(
            company_name=Subquery(
                CompanyName.objects.filter(id=OuterRef('comname_id')).values('company_name')[:1]
            )
        ).values('id','protype_id','product_type','proname_id','product_name','comname_id','company_name','product_weight','product_units','product_quantity','sell_amount','total_amount','ret_validity','ret_percentage','ret_amount','exc_validity','exc_percentage','exc_amount')
    
    for item in data:
        item['date'] = item['date'].strftime('%Y-%m-%d')
    
    queryset_dict = list(data)
    
    context = {
        'heading': queryset_dict,
        # Add more context variables as needed
    }

    # Render the HTML template with the context
    # html_content = render_to_string('pdfTemplate/your_template.html', context)
    html_content = render_to_string('billmgmt/billPDF.html', context)
    
    

    # Configure options as needed
    options = {
        'page-size': 'A4',
        'encoding': 'UTF-8',
        # Include more options as per your requirements
    }

    # Generate PDF from HTML content
    pdf = pdfkit.from_string(html_content, False, options=options)

    # Prepare HTTP response with PDF content as attachment
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="hindi_content.pdf"'

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
    