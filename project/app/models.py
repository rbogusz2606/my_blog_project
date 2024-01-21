from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.


class Activities(models.Model):
    name = models.CharField(max_length = 25)
    description = models.TextField(max_length = 10000)
    image = models.ImageField(default= None, null= True, upload_to= "photos/photos")

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("activity_detail", args=[self.id])
    

class UserHobby(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, default = None)
    hobby = models.TextField( max_length=10000, blank=False, null=False)
    image = models.ImageField(default= None, null= True, blank=True, upload_to= "images/photos")
    
    def __str__(self):
        return self.author.username
    
    
    
    
    
    
    
