from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import ProductType, Product
 
# Create your views here.
 
def merchstore_list(request):
    product_type = ProductType.objects.all()
    
    return render(request, 'merchstore_list.html', {'product_type':product_type})

def merchstore_detail(request, param):
	product_type = ProductType.objects.get(id=param)
    product = Product.objects.filter(product_type=product_type)

    return render(request, 'merchstore_detail.html', {'product_type':product_type, 'product':product})