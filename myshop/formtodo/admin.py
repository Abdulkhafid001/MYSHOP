from django.contrib import admin


# Register your models here.
# steps to register a model
# Step 1: we have to import the model from our model module into the admin module
from formtodo.models import Customer, TodoList
# Step 2: register the model (database table)
admin.site.register(Customer)
admin.site.register(TodoList)