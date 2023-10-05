from django.db import models

# Create your models here.
# i have to come up with a way to store this number of votes and result and arrange them by highest winner


class CandidateInfo(models.Model):
    candidate_name = models.CharField(max_length=100)
    candidate_state = models.CharField(max_length=20)
    desired_post = models.CharField(max_length=100)


class ElectionResult(models.Model):
    votes = models.IntegerField(default=0)
