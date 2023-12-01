from django.db import models
from django.contrib.auth.models import User
from datetime import date
    
class Blog(models.Model):
    title=models.CharField(max_length=80)
    date=models.DateField(default=date.today)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    content=models.CharField(max_length=250)

    class Meta:
        ordering = ('-date',)

    def __str__(self):
        return self.title
    