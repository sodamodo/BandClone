from django.http import HttpResponse
from Rocker.models import Post
from django.shortcuts import render

def hello(request):
    posts = Post.objects.all()
    return render(request, 'base.html', {'blog': posts})

def register(request):
    return render(request,'register.html',{'hello':"hello"})