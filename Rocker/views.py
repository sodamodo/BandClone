from django.http import HttpResponse
from Rocker.models import Post
from django.shortcuts import render
from django.contrib.auth.models import User

def hello(request):
    posts = Post.objects.all()
    return render(request, 'base.html', {'blog': posts})

def register(request):
    return render(request,'register.html',{'hello':"hello"})

def createuser(request):
    pass