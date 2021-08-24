from django.shortcuts import render,HttpResponse,redirect
from Login.models import Login
from django.contrib.auth.hashers import make_password
from django.contrib import admin
# Create your views here.
def login(request):
    
    if request.method=="POST":
        type=request.POST.get('value')
        email=request.POST.get('email')
        password=make_password(request.POST.get('password'))
        
        context={
            'type':type
        }
        if type=="Admin":

            login=Login(email=email,password=password,is_super_user=True)
            login.save()
            
            return redirect('/admin')
        else:
            login=Login(email=email,password=password,is_super_user=False)
            login.save()
            return redirect('/user')
            
    
    return render(request,'index.html')
def user(request):
    return render(request,'user.html')