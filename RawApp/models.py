from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    CHOICES = ( 
    ("male","Male"), ("female","Female"), ("nonbinary","Rather not say")
    )
    username = models.CharField(max_length=30, unique =True)
    password = models.CharField(max_length=128)
    email = models.EmailField(max_length=128,unique =True)
    gender = models.CharField(max_length=30, choices = CHOICES, default="nonbinary")
    time = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.username


