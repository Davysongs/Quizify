from django.db import models
from base.models import Quiz
from django.contrib.auth.models import User

# Create your models here.
class Result(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete= models.SET_DEFAULT, default ="")
    user = models.ForeignKey(User,on_delete= models.SET_DEFAULT, default="")
    score = models.FloatField()
    result_id = models.CharField(max_length=15, primary_key = True)
    date = models.DateTimeField(auto_now_add = True)
    question_ans = models.CharField(max_length = 1000)
    answer_status = models.CharField(max_length = 1000)
    status = models.CharField(max_length = 6)


    def __str__(self):
        return str(self.pk)