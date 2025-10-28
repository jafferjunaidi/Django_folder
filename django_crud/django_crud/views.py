from Std_records.models import Student
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib import messages

def Addstudent(req):
    if req.method == "POST":
        name = req.POST.get("std_name")
        age = req.POST.get("std_age")
        city = req.POST.get("std_city")
        mail = req.POST.get("std_mail")

        if not name or not age or not city or not mail:
            messages.error(req, "All fields are required")
        else:
            try:
                Student.objects.create(
                    std_name=name,
                    std_age=int(age),
                    std_city=city,
                    std_mail=mail
                )
                messages.success(req, "Record inserted successfully")
                return redirect("addstd")
            except Exception as e:
                messages.error(req, f"Error: {e}")

    # ✅ Always return a response, even for GET requests
    return render(req, "form.html")

def Showstudent(req):
    std=Student.objects.all()
    return render(req,"fetch_data.html",{"students":std})

def Delstudent(req,id):
    try:
        std=Student.objects.get(id=id)
        std.delete()
        messages.success(req,"Record deleted successfully")
        return redirect("showstd")
    except Student.DoesNotExist:
        messages.error(req,"Student not found")
        return redirect("showstd")

def Editstudent(req,id):
    std = get_object_or_404(Student,id=id)
    try:
        if req.method=="POST":
            sname=req.POST.get("std_name")
            sage=req.POST.get("std_age")
            scity=req.POST.get("std_city")
            smail=req.POST.get("std_mail")
            
            std.std_name=sname
            std.std_age=sage
            std.std_city=scity
            std.std_mail=smail
            
            std.save()
            messages.success(req,"Record updated successfully")
            return redirect("showstd")
            
    except Exception as e:
        messages.error(req,f"Error:{e}")
    return render(req,"edit_data.html",{"students":std})