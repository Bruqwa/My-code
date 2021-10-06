from django.shortcuts import render
from django.views import generic
from .models import Blog_post
from .models import About
from django.http import HttpResponse
from django.http import Http404
from django.template import loader

# Create your views here.

def index(request):
	return render(request, 'mysite/index.html')

def about(request):
	about_objects = About.objects.all()
	cont = {'about_objects':about_objects}
	return render(request, 'mysite/about.html', cont)

def blog(request):
	blog_list = Blog_post.objects.all()
	cont = {'blog_list':blog_list}
	return render(request, 'mysite/blog.html', cont)

def contacts(request):
	return render(request, 'mysite/contacts.html')

def goods(request):
	return render(request, 'mysite/goods.html')