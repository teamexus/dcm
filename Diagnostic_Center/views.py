from django.shortcuts import render
from django.contrib.auth.models import User 
from .models import *
from django.contrib.auth import authenticate, logout, login

# Create your views here.

def blog_list(request):
    return render(request, 'Diagnostic_Center/blog_list.html', context={})


