from django.db import models

# Create your models here.


class Customer(models.Model):
    customer_name = models.CharField(max_length=200)
    customer_lastname = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.customer_name + " " + self.customer_lastname

# model for my todo-list


class TodoList(models.Model):
    task_name = models.CharField(max_length=200)
    task_priority = models.BooleanField()
    date = models.DateTimeField()
