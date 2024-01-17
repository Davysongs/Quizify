from django.db import models

# Create your models here.
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
