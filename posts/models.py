from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.


class Post(models.Model):

    title =models.CharField(max_length=50)
    slug =models.CharField(max_length=255,unique=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    updated =models.DateTimeField(auto_now=True)
    created_at=models.DateTimeField(auto_now_add=True)
    content = models.TextField()
       
    class Meta:
        ordering = ['-created_at']


    def __str__(self) -> str:
        return self.title 

