from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class User(models.Model):
    CHOICES = ( 
    ("male","Male"), ("female","Female"), ("nonbinary","Rather not say")
    )
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=128)
    email = models.EmailField()
    gender = models.CharField(max_length=30, choices = CHOICES, default="nonbinary")
    def __str__(self):
        return self.username
