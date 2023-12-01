from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView
from .models import Blog
from django.contrib.auth.models import User

class HomePage(TemplateView):
    template_name='homepage.html'

class BlogList(ListView):
    queryset=Blog.objects.all()
    template_name='blog_list.html'
    context_object_name='blog_list'
    paginate_by=5

class BlogDetail(DetailView):
    model=Blog
    template_name='blog_detail.html'
    context_object_name='blog'

class AuthorDetail(DetailView):
    model=User
    template_name='author_detail.html'
    context_object_name='author'