from django.contrib.auth import authenticate, login,logout
from django.http.response import HttpResponseRedirect
from ecom.settings import TEMPLATES
from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from .models import  order,consumer
from django.contrib import messages
import pandas as pd
from django.http.request import HttpRequest
from django.views.decorators.csrf import csrf_exempt

def home(request):
    return render(request, 'product/home.html')
def products(request):
    return render(request,'product/products.html')

def list_orders(request):
    order_list=order.objects.all()
    return render(request,'product/first.html',{'order_list':order_list})

def consumers(request):
    c_list=consumer.objects.all()
    return render(request,'product/customer.html',{'c_list':c_list})
def signin(request):
            return render(request, 'product/login.html')

'''
    # if request.user.is_authenticated(): # if user is already logged in
     #   return HttpResponseRedirect('/') # SHOULD BE DASHBOARD
     if request.method == 'POST':
        pass
        if request.is_valid():
            username = request.cleaned_data['username']
            password = request.cleaned_data['password']
            user = authenticate(username=username, password=password) #returns None
            if user is not None:
                login(request, user)
                return redirect('products') # SHOULD BE DASHBOARD
            else:
                messages.success(request,(' Do not lie with the credentials'))
                return redirect('login')
        else:
            return render(request, 'login.html')
     
    else: 
        form = LoginForm()
        context = {'form': form}
'''
def forgot(request):
    return render(request,'product/forgot.html')

@csrf_exempt
def upload(request):
    if request.method == 'GET':
     return render(request,'product/upload.html')#data=file.to_html())
    if request.method =='POST':
        file=request.POST.get('uploads')
        
        return render(request,'product/display.html',{'data':file})
        #open_file=pd.read_csv(file)
   #     return render(request,'display.html',data=file.to_html())

def specific(request):
    return render(request,'product/specific-order.html')

def display(request):
    return render(request,'product/display.html')