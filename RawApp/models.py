from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=30)
    password = models.OneToOneField(User, on_delete = models.CASCADE)
    email = models.EmailField()
    def __str__(self):
        return self.username
