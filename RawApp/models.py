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
    time = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.username
class Questions(models.Model):
    TOPICS = (
        ("General-Studies", "General Studies"), ("history", "history"), ("Current-Affairs", "Current Affairs"), ("Mathematics", "Mathematics")
    )
    question = models.CharField(max_length= 1000)
    optionA = models.CharField(max_length=200)
    optionB = models.CharField(max_length=200)
    optionC = models.CharField(max_length=200)
    optionD = models.CharField(max_length=200) 
    category = models.CharField(max_length=20, choices= TOPICS)
