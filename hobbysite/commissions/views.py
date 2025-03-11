from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Commission, Comment

# Create your views here.
def commission_list(request):
    commissions = Commission.objects.order_by("created_on")
    #return

def comment_list(request):
    comments = Comment.objects.objects.order_by("-created_on")
    #return