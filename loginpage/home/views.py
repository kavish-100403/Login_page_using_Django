from django.shortcuts import render,HttpResponse,redirect
from datetime import datetime
from home.models import Register
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from django.contrib.auth import login
from django.contrib.auth.models import User





# Create your views here.

def mainpage(request):
    return render(request,'mainpage.html')

# def loginUser(request):
#     if request.method=="POST":
#         username=request.POST.get('username')
#         password=request.POST.get('password')
#         print(username,password)
#         # print(Register.objects.filter(username=usern))

#         #To check if the user has entered correct credentials
#         user = authenticate(username=username, password=password)
#         if user is not None:
#              # A backend authenticated the credentials
#             login(request, user)
#             return redirect("/form")
#         else:
#     # No backend authenticated the credentials
#             return render(request,"mainpage.html")
        
#     return(render(request,'mainpage.html'))

# def logoutUser(request):
#     logout(request)
#     return redirect("/login")


def register(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        username=request.POST.get('username')
        password=request.POST.get('password')
        phone=request.POST.get('phone')

        #user will create a new user for logging in to the database
        user = User.objects.create_user(username,email,password)
        user.save()

        #register will save the user credentials to the database
        register=Register(name=name,email=email,username=username,password=password,phone=phone,date=datetime.today())
        register.save()
    return render(request,'register.html')


    # messages.success(request, "Profile details updated.")
    # return render(request,'register.html')
def form(request):
    return render(request,'form.html')
