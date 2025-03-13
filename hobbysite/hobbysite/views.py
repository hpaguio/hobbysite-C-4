from django.shortcuts import render

def homepage(request):
    return render(request, "home.html")  # This will use a 'home.html' template