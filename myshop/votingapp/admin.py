from django.contrib import admin

# Register your models here.

# steps to register a model
# Step 1: we have to import the model from our model module into the admin module
from .models import Question,Choice
# Step 2: register the model (database table)
admin.site.register(Question)
# Step 2: register the model (database table)
admin.site.register(Choice)