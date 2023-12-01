from django.contrib import admin
from django.urls import path
from blog_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/',views.HomePage.as_view(),name='homepage'),
    path('blog/blogs/',views.BlogList.as_view(),name='blog_list'),
    path('blog/<int:pk>/',views.BlogDetail.as_view(),name='blog'),
    path('blog/blogger/<int:pk>/',views.AuthorDetail.as_view(),name='author'),
]
