from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from django.contrib.auth import login

# Create your views here.

def mainpage(request):
    return render(request,'mainpage.html')
def register(request):
    return render(request,'register.html')
def form(request):
    return render(request,'fomr.html')
