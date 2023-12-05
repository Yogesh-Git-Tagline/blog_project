from django.contrib import admin
from .models import Blog,BlogComment

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display=['id','title','created_at','modified_at','author','content']

@admin.register(BlogComment)
class BlogCommentAdmin(admin.ModelAdmin):
    list_display=['id','description','for_blog','created_at']
