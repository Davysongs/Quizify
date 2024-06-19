from django.db import models
import random

# Create your models here.
ALLCHOICES = (
    ("easy","easy"),
    ("medium","medium"),
    ("hard","hard"),
)
class Quiz(models.Model):
    name = models.CharField(max_length=50)
    topic = models.CharField(max_length=50)
    quiz_length = models.IntegerField()
    time = models.IntegerField(help_text = "minutes")
    pass_mark = models.IntegerField(help_text = "minimum required score")
    difficulty = models.CharField(max_length =10, choices = ALLCHOICES ) 

    def __str__(self):
        return f"{self.name}-{self.topic}"
    
    def getquestions(self):
        questions = list(self.question_set.all())
        random.shuffle(questions)
        return questions[:self.quiz_length]
    
    class Meta:
        verbose_name_plural = "Quizes"



