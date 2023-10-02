from django.db import models
import polls.mycode as mycode
# Create your models here.
# this will store all the models for the application
""" the todoitem database """
class TodoItem(models.Model):
    title = models.CharField(max_length=200)
    date_and_time = models.DateTimeField(mycode.get_time_date, max_length=20)
    completed = models.BooleanField(default=False)
# create a model for my polling app
class Poll(models.Model):
    candidate_name = models.CharField(max_length=20)
    candidate_state = models.CharField(max_length=10)
    vote = models.IntegerField(auto_created=1)
    number_of_vote = models.Count(vote)