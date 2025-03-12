from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Commission, Comment

# Create your views here.
def commission_list(request):
    commissions = Commission.objects.order_by("created_on")
    
    return render(request, 'commissions_list', {'commission':commissions})

def commission_details(request, param):
    commissions = Commission.objects.get(id=param)
    comments = Comment.objects.objects.order_by("-created_on")

    return render(request, 'commissions_detail.html', {'commission':commissions, 'comments':comments})