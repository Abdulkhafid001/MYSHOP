from django.contrib import admin
 
# Register your models here.
# steps to register a model
# Step 1: we have to import the model from our model module into the admin module
from .models import TodoItem
from .models import Poll
# Step 2: register the model (database table)
admin.site.register(TodoItem)
# Step 2: register the polling model (database table)
admin.site.register(Poll)
