from django.shortcuts import render
from django.http import HttpResponse, request

# Create your views here.
def signin(request):
    return render(request, 'members/login.html')