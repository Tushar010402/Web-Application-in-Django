from django.shortcuts import render, HttpResponse
from datetime import datetime
from tushar.models import Contact
def index(request):
    return render(request,'index.html')

# Create your views here.
def about(request):
    return render(request,'about.html')
def services(request):
    return render(request,'services.html')
def contact(request):
    if request.method == "POST":
        print(request)
        First_Name = request.POST.get('First_Name','')
        Last_Name = request.POST.get('Last_Name','')
        Phone = request.POST.get('Phone','')
        Email = request.POST.get('Email','')
        desc = request.POST .get('desc','')
        contact = Contact(First_Name=First_Name, Last_Name=Last_Name, Phone=Phone, Email=Email, desc=desc, date=datetime.today())
        contact.save()
    return render(request,'Contact.html')

