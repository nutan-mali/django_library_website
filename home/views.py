from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact 
from django.contrib import messages
# Create your views here.
def index(request):
    # messages.success(request,'this is test msg')
    return render(request,'index.html')
    # return HttpResponse('this is my first command on django.successfully run!')

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')
    

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name , email=email , phone=phone, desc=desc , date=datetime.today() )
        contact.save()
        messages.success(request, "Your Message has been sent Successfully!")
    return render(request,'contact.html')
   
