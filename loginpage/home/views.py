from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Register
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from django.contrib.auth import login




# Create your views here.

def mainpage(request):
    return render(request,'mainpage.html')
def register(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        username=request.POST.get('username')
        password=request.POST.get('password')
        phone=request.POST.get('phone')

        register=Register(name=name,email=email,username=username,password=password,phone=phone,date=datetime.today())
        register.save()
    return render(request,'register.html')
    # messages.success(request, "Profile details updated.")
    # return render(request,'register.html')
def form(request):
    return render(request,'form.html')
