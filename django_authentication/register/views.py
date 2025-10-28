from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def Signup(req):
    if req.method=="POST":
        uname=req.POST.get("username")
        mail=req.POST.get("email")
        pin=req.POST.get("password")
        # print(uname,mail,pin)
        user=User.objects.create_user(username=uname,email=mail,password=pin)
        return redirect("login")
    return render(req,"signup.html")

def Login(req):
    if req.method=="POST":
        uname=req.POST.get("username")
        pin=req.POST.get("password")
        #print(uname , pin)
        user=authenticate(req,username=uname,password=pin)
        if user is not None:
            login(req,user)
            return redirect("home")
    return render(req,"login.html")

def Logout(req):
    logout(req)
    # return render(req,"login.html")
    return redirect("login")

@login_required
def Home(req):
    return render(req,"index.html")

# django_admin
# username=jaffer2003
# password=*4321*