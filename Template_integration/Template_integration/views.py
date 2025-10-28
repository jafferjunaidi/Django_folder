from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,"index.html")

def about(request): 
    return render(request,"about.html")

def contact(request):
    return HttpResponse("<h2>This is contact page</h2>")