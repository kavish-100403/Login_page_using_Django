from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Register
from django.contrib import messages



# Create your views here.

def mainpage(request):
    return render(request,'mainpage.html')
def register(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        number=request.POST.get('number')

        register= Register(name=name,email=email,password=password, number=number,date=datetime.today())
        register.save()
    # return render(request,'register.html')
def form(request):
    return render(request,'fomr.html')
