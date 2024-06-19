from django.db import models
from base.models import Quiz

# Create your models here.
class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete = models.CASCADE) 
    text = models.CharField(max_length= 300)
    date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.text)
    
    def get_answers(self):
        return self.answer_set.all()
class Answer(models.Model):
    text = models.CharField(max_length= 300)
    correct = models.BooleanField(default  = False)
    question = models.ForeignKey(Question , on_delete = models.CASCADE)
    date = models.DateTimeField(auto_now_add = True)

    def __str__ (self):
        return f"question:{self.question.text}, answer: {self.text}, correct: {self.correct}"