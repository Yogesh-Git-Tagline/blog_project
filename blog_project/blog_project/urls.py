from django.contrib import admin
from django.urls import path
from blog_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', views.HomePage.as_view(), name='homepage'),
    path('blog/blogs/', views.BlogList.as_view(), name='blog_list'),
    path('blog/<int:pk>/', views.BlogDetail.as_view(), name='blog'),
    path('blog/blogger/<int:pk>/', views.AuthorDetail.as_view(), name='author'),
    path('blog/<int:id>/create', views.AddBlogComment.as_view(), name='add_comment'),

    path('accounts/user_registeration/',
         views.UserRegistration.as_view(), name='user_register'),
    path('accounts/user_login/', views.UserLogin.as_view(), name='user_login'),
    path('logout/', views.UserLogout.as_view(), name='user_logout'),
]
