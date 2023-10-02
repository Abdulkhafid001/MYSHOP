from django.db import models

# Create your models here.
# this module has two models: 1. QuestionModel A Question has a question and a publication date.
# the Choice has two fields: the text of the choice and a vote tally. Each Choice is associated with a Question.
class Question(models.Model):
    # created a char column
    question_text = models.CharField(max_length=100)
    # created a datetimefield
    pub_date = models.DateTimeField("date published")


class Choice(models.Model):
    # the two models are associated using a foreign key 
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # created choice column
    choice_text = models.CharField(max_length=200)
    # created a vote field
    votes = models.IntegerField(default=0)