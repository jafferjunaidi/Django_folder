from django.shortcuts import render, redirect

def form(req):
    if req.method == "GET" and req.GET:  # check if form is submitted
        name = req.GET.get("fname")
        age = req.GET.get("age")
        city = req.GET.get("city")

        # Store data in session (or pass via query params)
        req.session["myname"] = name
        req.session["myage"] = age
        req.session["mycity"] = city

        return redirect("message")  # redirect to message page

    return render(req, "form.html")  # just show empty form


def message(req):
    data = {
        "myname": req.session.get("myname"),
        "myage": req.session.get("myage"),
        "mycity": req.session.get("mycity"),
    }
    return render(req, "message.html", data)


# def form(req):
#     if req.method == "POST":   # check if form submitted
#         num1 = int(req.POST.get("num1"))
#         num2 = int(req.POST.get("num2"))
#         total = num1 + num2
#         # total = num1 - num2
        
#         # Save result in session so we can access it on message page
#         req.session["total"] = total

#         return redirect("message")
#     return render(req, "form.html")  # just show the form initially

# def message(req):
#     data = {"total": req.session.get("total")}
#     return render(req, "message.html", data)
      

