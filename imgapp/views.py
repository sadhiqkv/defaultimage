from django.shortcuts import render,redirect
from imgapp.models import product
import os

# Create your views here.
def index(request):
    return render(request,'add_product.html')

def add_product(request):
    if request.method=='POST':
        pname=request.POST['p1name']
        qty=request.POST['q1ty']
        price=request.POST['p1rice']
        if request.FILES.get('f1ile') is not None:
            simage=request.FILES['f1ile']
        else:
            simage="/static/images/83.jpg"
        product1=product(product_name=pname,quantity=qty,price=price,image=simage)
        product1.save()
        return redirect('show_products')

def show_products(request):
   products=product.objects.all()
   return render(request,'show_product.html',{'products':products})         

def editpage(request,id):
    products=product.objects.get(id=id)
    return render(request,'Edit.html',{'products':products}) 
#edit page..
def edit_product_details(request,id):
    if request.method=='POST':
        products=product.objects.get(id=id)
        products.product_name=request.POST.get('product_name')
        products.quantity=request.POST.get('quantity')
        products.price=request.POST.get('price')
        if request.FILES.get('file') is not None:
            print(products.image)
            if products.image== "/static/images/83.jpg":
                # os.remove(products.image.path)
                products.image=request.FILES['file']
            else:
                os.remove(products.image.path)
                products.image=request.FILES['file']    
        else:
            os.remove(products.image.path)
            products.image="/static/images/83.jpg"             
        products.save()
        return redirect('show_products')
    return render(request,'Edit.html') 
def delete(request,id):
    prd=product.objects.get(id=id)
    prd.delete()
    return redirect('show_products')  
 