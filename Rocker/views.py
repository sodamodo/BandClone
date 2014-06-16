from django.http import HttpResponse
from Rocker.models import Post
from django.shortcuts import render

def hello(request):
    posts = Post.objects.all()
    return render(request, 'base.html', {'blog': posts})