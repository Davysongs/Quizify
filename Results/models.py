from django.db import models
from RawApp.models import Quiz
from django.contrib.auth.models import User

# Create your models here.
class Result(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete= models.CASCADE)
    user = models.ForeignKey(User,on_delete= models.CASCADE)
    score = models.FloatField()
    result_id = models.CharField(max_length=13, primary_key = True)
    date = models.DateTimeField(auto_now_add = True)
    options_selected = models.CharField(max_length = 1000, default = None)
    

    def __str__(self):
        return str(self.pk)