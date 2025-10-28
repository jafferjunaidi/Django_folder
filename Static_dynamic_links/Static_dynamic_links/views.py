from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Static Dynamic Links project!")

def home(request,sid):
    return HttpResponse(sid) 

def about(request):
    return HttpResponse("This is the about page of the Static Dynamic Links project!")