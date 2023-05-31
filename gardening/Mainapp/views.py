from django.shortcuts import render ,HttpResponseRedirect
from .models import *

# Create your views here.
def homepage(request):
    data = services.objects.all().order_by("id")
    

    if request.method == "POST":
        Q = Quote()
        Q.name = request.POST.get("name")
        Q.email = request.POST.get("email")
        Q.service_type = request.POST.get("service_type")
        Q.phone = request.POST.get("phone")
        Q.msgs = request.POST.get("msg")
        Q.save()

    return render(request,"index.html",{"data" : data})
def errorpage(request):
    return render(request,"404.html")

def aboutpage(request):
    return render(request,"about.html")

def contactpage(request):
    if request.method == "POST":
      c = Contact()
      c.name = request.POST.get("name")
      c.email = request.POST.get("email")
      c.subject = request.POST.get("subject")
      c.msgs = request.POST.get("msgs")
      c.save()
      return render(request,"contact.html")

    
    return render(request,"contact.html")

def projectpage(request):
    return render(request,"project.html")

def featurepage(request):
    return render(request,"feature.html")

def quotepage(request):
    if request.method == "POST":
        Q = Quote()
        Q.name = request.POST.get("name")
        Q.email = request.POST.get("email")
        Q.service_type = request.POST.get("service_type")
        Q.phone = request.POST.get("phone")
        Q.msgs = request.POST.get("msg")
        Q.save()

    return render(request,"quote.html")

def servicepage(request):
    data = services.objects.all().order_by("id")
    return render(request,"service.html" ,{"data" :data})

def teampage(request):
    return render(request,"team.html")

def testimonialpage(request):
    return render(request,"testimonial.html")

def descriptionpage(request,num):
   data = services.objects.get(id=num)
   return render(request,"description.html",{"data":data})



