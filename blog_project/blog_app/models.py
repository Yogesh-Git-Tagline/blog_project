from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.urls import reverse

class BlogDate(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Blog(BlogDate):
    title = models.CharField(max_length=500)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blogs')
    content = models.TextField()

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog", kwargs={"pk": self.pk})


class BlogComment(BlogDate):
    description = models.TextField()
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    commentor = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ('-created_at',)
