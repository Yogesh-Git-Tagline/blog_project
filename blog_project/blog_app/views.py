from django.urls import reverse
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from .models import Blog, BlogComment
from django.contrib.auth.models import User
from .forms import BlogCommentForm, RegisterUserForm, LoginUserForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin


class HomePage(TemplateView):
    template_name = 'homepage.html'


class BlogList(ListView):
    template_name = 'blog_list.html'
    context_object_name = 'blog_list'
    paginate_by = 5

    # searching
    def get_queryset(self):
        blog_title = self.request.GET.get('search')
        if blog_title:
            return Blog.objects.filter(title__icontains=blog_title)
        return Blog.objects.all()


class BlogDetail(DetailView):
    model = Blog
    template_name = 'blog_detail.html'
    context_object_name = 'blog'


class AuthorDetail(DetailView):
    model = User
    template_name = 'author_detail.html'
    context_object_name = 'author'


class AddBlogComment(LoginRequiredMixin, CreateView):
    form_class = BlogCommentForm
    template_name = 'add_comment.html'
    context_object_name = 'form'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        self.url_id = self.kwargs['id']
        return kwargs

    def form_valid(self, form):
        blog_instance = Blog.objects.get(id=self.kwargs['id'])
        form.instance.for_blog = blog_instance
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blogpost'] = Blog.objects.get(id=self.url_id)
        return context

    def get_success_url(self):
        id = self.kwargs['id']
        return reverse('blog', kwargs={'pk': id})

# User Authentications


class UserRegistration(CreateView):
    form_class = RegisterUserForm
    template_name = 'user_authentication/user_registration.html'
    context_object_name = 'form'
    success_url = '/accounts/user_login/'


class UserLogin(LoginView):
    authentication_form = LoginUserForm
    template_name = 'user_authentication/user_login.html'
    context_object_name = 'form'
    success_url = '/blog/'


class UserLogout(LogoutView):
    template_name = 'user_authentication/user_login.html'
