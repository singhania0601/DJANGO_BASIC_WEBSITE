from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
# Create your views here.
def index(request):
    context = {}
    context = {
        "variable" : "this is sent"
    }
    return render(request,"index.html",context)
def services(request):
    return render(request,"services.html")
def about(request):
    return render(request,"about.html")
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip = request.POST.get('zip')
        contact = Contact(name = name,phone = phone, email = email, city = city, state = state, zip = zip, date= datetime.today())
        contact.save()
        messages.success(request, 'Your Form is submitted')

    return render(request,"contact.html")