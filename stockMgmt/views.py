from django.shortcuts import render
from .models import ProductType, ProductName, CompanyName, StockMgmt
from billMgmt.models import BillMgmt
from django.contrib import messages 
from django.http import HttpResponseRedirect,JsonResponse
from django.db.models import F, OuterRef, Subquery, Sum

# Create your views here.

def stockView(r):
    pro_typ_list = ProductType.objects.filter(delete=0)
    if r.method=='POST':
        s_stock_type = r.POST['s_stock_type']
        s_product_type = r.POST.get('s_product_type', '') 
        s_product_name = r.POST.get('s_product_name', '')  # Use '' as the default value
        s_company_name = r.POST.get('s_company_name', '') # Use '' as the default value
        from_date = r.POST['from_date']
        to_date = r.POST['to_date']
        
        stock_list = StockMgmt.objects.filter(delete=0,date__range=[from_date, to_date]).annotate(
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
        ).values('id','protype_id','product_type','proname_id','product_name','comname_id','company_name','stock_type','dealer_name','dealer_mob_number','dealer_address','date','product_weight','product_quantity','purchase_amount')
        
        if s_stock_type:
            stock_list = stock_list.filter(stock_type=s_stock_type)
            
        if s_product_type:
            stock_list = stock_list.filter(protype_id=s_product_type)
        
        if s_product_name:
            stock_list = stock_list.filter(proname_id=s_product_name)
            
        if s_company_name:
            stock_list = stock_list.filter(proname_id=s_company_name)
        
        for item in stock_list:
            item['date'] = item['date'].strftime('%Y-%m-%d')
            
        print(stock_list)
        
        product_stock_list = ProductName.objects.filter(delete=0).annotate(
                product_type=Subquery(
                    ProductType.objects.filter(id=OuterRef('protype_id')).values('product_type')[:1]
                )
            ).values('id','protype_id','product_type','product_name')
        
        for sitem in product_stock_list:
            
            total_stock_quantity = StockMgmt.objects.filter(proname_id=sitem['id']).aggregate(
                total_stock_quantity=Sum('product_quantity')
            )['total_stock_quantity'] or 0
            
            total_bill_quantity = BillMgmt.objects.filter(proname_id=sitem['id']).aggregate(
                total_bill_quantity=Sum('product_quantity')
            )['total_bill_quantity'] or 0
            
            sitem['total_stock_quantity'] = total_stock_quantity
            sitem['total_bill_quantity'] = total_bill_quantity
            sitem['total_bal_quantity'] = total_stock_quantity - total_bill_quantity
        
    else :
        stock_list = StockMgmt.objects.filter(delete=0).annotate(
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
        ).values('id','protype_id','product_type','proname_id','product_name','comname_id','company_name','stock_type','dealer_name','dealer_mob_number','dealer_address','date','product_weight','product_quantity','purchase_amount')
        
        for item in stock_list:
            item['date'] = item['date'].strftime('%Y-%m-%d')
            
        product_stock_list = ProductName.objects.filter(delete=0).annotate(
                product_type=Subquery(
                    ProductType.objects.filter(id=OuterRef('protype_id')).values('product_type')[:1]
                )
            ).values('id','protype_id','product_type','product_name')
        
        for sitem in product_stock_list:
            
            total_stock_quantity = StockMgmt.objects.filter(proname_id=sitem['id']).aggregate(
                total_stock_quantity=Sum('product_quantity')
            )['total_stock_quantity'] or 0
            
            total_bill_quantity = BillMgmt.objects.filter(proname_id=sitem['id']).aggregate(
                total_bill_quantity=Sum('product_quantity')
            )['total_bill_quantity'] or 0
            
            sitem['total_stock_quantity'] = total_stock_quantity
            sitem['total_bill_quantity'] = total_bill_quantity
            sitem['total_bal_quantity'] = total_stock_quantity - total_bill_quantity
        
        # print(product_stock_list)
            
    return render(r, 'stockmgmt/stockmgmt.html',{'pro_typ_list':pro_typ_list, 'stock_list':stock_list, 'product_stock_list':product_stock_list})

def getCompanyName(r):
    product_type = r.GET.get('product_type') # get question id from question list in jyo_questions 
    product_name = r.GET.get('product_name')
    company_name_list = CompanyName.objects.filter(delete=0,proname_id = product_name, protype_id = product_type).values('id','protype_id','proname_id','company_name')
    
    return JsonResponse({'company_name_list': list(company_name_list)})

def postStock(r):
    user_id = r.session.get('user_id')
    
    if r.method=='POST':
        edit_id = r.POST['edit_id']
        product_type = r.POST['product_type']
        product_name = r.POST['product_name']   
        company_name = r.POST['company_name']
        stock_type = r.POST['stock_type']
        dealer_name = r.POST['dealer_name']
        dealer_mob_number = r.POST['dealer_mob_number']
        dealer_address = r.POST['dealer_address']
        date = r.POST['date']
        product_weight = r.POST['product_weight']
        product_quantity = r.POST['product_quantity']
        purchase_amount = r.POST['purchase_amount']
        

        if edit_id:
            #This is for Update Jyotishi Question
            obj = StockMgmt.objects.get(id=edit_id)
            obj.protype_id = product_type
            obj.proname_id = product_name
            obj.comname_id = company_name
            obj.stock_type = stock_type
            obj.dealer_name = dealer_name
            obj.dealer_mob_number = dealer_mob_number
            obj.dealer_address = dealer_address
            obj.date = date
            obj.product_weight = product_weight
            obj.product_quantity = product_quantity
            obj.purchase_amount = purchase_amount
            obj.save()
            
            messages.success(r, 'Stock Management Updated Successfully.')
        else:
            #This is for Create Jyotishi Question
            obj = StockMgmt(
                protype_id = product_type,
                proname_id = product_name,
                comname_id = company_name,
                stock_type = stock_type,
                dealer_name = dealer_name,
                dealer_mob_number = dealer_mob_number,
                dealer_address = dealer_address,
                date = date,
                product_weight = product_weight,
                product_quantity = product_quantity,
                purchase_amount = purchase_amount,
                delete=0,
                a_id=user_id)
            obj.save()
            #if product_name is created successfully then if block will be executed
            if obj:
                messages.success(r, 'Stock Management Added Successfully.')
            else:
            #if product_name is not created successfully then else block will be executed
                messages.error(r, 'Stock Management Added UnSuccessfully.')
    #Redirect to Jyotishi Question List     
    return HttpResponseRedirect("/stockmgmt/stock_view/")

def stockMgmtDelete(r,id):
    obj = StockMgmt.objects.get(id=id)
    obj.delete = 1
    obj.save()
    messages.success(r, 'Stock Management Deleted Successfully.')
    #Redirect to Jyotishi Question List   
    return HttpResponseRedirect("/stockmgmt/stock_view/")
################################################################################################

def productTypeView(r):
    pro_typ_list = ProductType.objects.filter(delete=0)
    return render(r, 'stockmgmt/producttype.html',{'pro_typ_list':pro_typ_list })

def postproType(r):
    user_id = r.session.get('user_id')
    
    if r.method=='POST':
        edit_id = r.POST['edit_id']
        product_type = r.POST['product_type']

        if edit_id:
            #This is for Update Jyotishi Question
            obj = ProductType.objects.get(id=edit_id)
            obj.product_type = product_type
            obj.save()
            
            messages.success(r, 'Product Type Updated Successfully.')
        else:
            #This is for Create Jyotishi Question
            obj = ProductType(
                product_type=product_type,
                delete=0,
                a_id=user_id
            )
            obj.save()
            #if product_type is created successfully then if block will be executed
            if obj:
                messages.success(r, 'Product Type Added Successfully.')
            
            else:
            #if product_type is not created successfully then else block will be executed
                messages.error(r, 'Product Type Added UnSuccessfully.')
                
    #Redirect to Jyotishi Question List     
    return HttpResponseRedirect("/stockmgmt/product_type/")

def proTypeDelete(r,id):
    obj = ProductType.objects.get(id=id)
    obj.delete = 1
    obj.save()
    messages.success(r, 'Product Type Deleted Successfully.')
    #Redirect to Jyotishi Question List   
    return HttpResponseRedirect("/stockmgmt/product_type/")

################################################################################################

def productNameView(r):
    pro_typ_list = ProductType.objects.filter(delete=0)
    
    pro_name_list = ProductName.objects.filter(delete=0).annotate(
        product_type=Subquery(
            ProductType.objects.filter(id=OuterRef('protype_id')).values('product_type')[:1]
        )
    ).values('id','protype_id','product_type', 'product_name')
     
    return render(r, 'stockmgmt/productname.html',{'pro_name_list':pro_name_list, 'pro_typ_list':pro_typ_list})

def postProName(r):
    user_id = r.session.get('user_id')
    
    if r.method=='POST':
        edit_id = r.POST['edit_id']
        product_name = r.POST['product_name']   
        product_type = r.POST['product_type']
        

        if edit_id:
            #This is for Update Jyotishi Question
            obj = ProductName.objects.get(id=edit_id)
            obj.product_name = product_name
            obj.protype_id = product_type
            obj.save()
            
            messages.success(r, 'Product Name Updated Successfully.')
        else:
            #This is for Create Jyotishi Question
            obj = ProductName(
                product_name=product_name,
                protype_id = product_type,
                delete=0,
                a_id=user_id)
            obj.save()
            #if product_name is created successfully then if block will be executed
            if obj:
                messages.success(r, 'Product Name Added Successfully.')
            else:
            #if product_name is not created successfully then else block will be executed
                messages.error(r, 'Product Name Added UnSuccessfully.')
    #Redirect to Jyotishi Question List     
    return HttpResponseRedirect("/stockmgmt/product_name/")

def proNameDelete(r,id):
    obj = ProductName.objects.get(id=id)
    obj.delete = 1
    obj.save()
    messages.success(r, 'Product Name Deleted Successfully.')
    #Redirect to Jyotishi Question List   
    return HttpResponseRedirect("/stockmgmt/product_name/")

################################################################################################

def companyNameView(r):
    pro_typ_list = ProductType.objects.filter(delete=0)
    
    company_name_list = CompanyName.objects.filter(delete=0).annotate(
            product_type=Subquery(
                ProductType.objects.filter(id=OuterRef('protype_id')).values('product_type')[:1]
            )
        ).annotate(
        product_name=Subquery(
            ProductName.objects.filter(id=OuterRef('proname_id')).values('product_name')[:1]
        )
    ).values('id','protype_id','product_type','proname_id','product_name','company_name')
        
        
    return render(r, 'stockmgmt/companyname.html',{'pro_typ_list':pro_typ_list,'company_name_list':company_name_list})

def getProductName(r):
    product_type = r.GET.get('product_type') # get question id from question list in jyo_questions 
    
    product_name_list = ProductName.objects.filter(delete=0,protype_id = product_type).values('id','protype_id','product_name')
    
    return JsonResponse({'product_name_list': list(product_name_list)})
    
def postCompanyName(r):
    user_id = r.session.get('user_id')
    
    if r.method=='POST':
        edit_id = r.POST['edit_id']
        product_name = r.POST['product_name']   
        product_type = r.POST['product_type']
        company_name = r.POST['company_name']

        if edit_id:
            #This is for Update Jyotishi Question
            obj = CompanyName.objects.get(id=edit_id)
            obj.proname_id = product_name
            obj.protype_id = product_type
            obj.company_name = company_name
            obj.save()
            
            messages.success(r, 'Company Name Updated Successfully.')
        else:
            #This is for Create Jyotishi Question
            obj = CompanyName(
                proname_id=product_name,
                protype_id = product_type,
                company_name = company_name,
                delete=0,
                a_id=user_id)
            obj.save()
            #if product_name is created successfully then if block will be executed
            if obj:
                messages.success(r, 'Company Name Added Successfully.')
            else:
            #if product_name is not created successfully then else block will be executed
                messages.error(r, 'Company Name Added UnSuccessfully.')
    #Redirect to Jyotishi Question List     
    return HttpResponseRedirect("/stockmgmt/company_name/")

def companyNameDelete(r,id):
    obj = CompanyName.objects.get(id=id)
    obj.delete = 1
    obj.save()
    messages.success(r, 'Company Name Deleted Successfully.')
    #Redirect to Jyotishi Question List   
    return HttpResponseRedirect("/stockmgmt/company_name/")

################################################################################################
