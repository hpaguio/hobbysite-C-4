from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import ProductType, Product
 
# Create your views here.
 

def list(request):
    product_type = ProductType.objects.order_by("name")
    #return

def detail(request):
    product = Product.objects.order_by("name")
    #return