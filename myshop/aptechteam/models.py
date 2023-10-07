from django.db import models

# Create your models here.
class Members(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    position = models.CharField(max_length=20, null=True)
    phone = models.IntegerField(null=True)
    joined_date = models.DateField(null=True)