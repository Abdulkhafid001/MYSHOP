from django.db import models

# Create your models here.
# testing how to use django with json
# create a model to get the data from admin


class Student(models.Model):
    # create a tuple with course-names and pass course with its number
    course_choices = (('1', 'java'), ('2', 'python'), ('3', 'javascript'))
    # create model fields
    name = models.CharField(max_length=100)
    rollno = models.IntegerField()
    course = models.CharField(max_length=15, choices=course_choices)


class Userweather(models.Model):
    city = models.CharField(max_length=100)
    lat = models.IntegerField()
    lon = models.IntegerField()
