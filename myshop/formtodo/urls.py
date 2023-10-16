from django.contrib import admin
from django.urls import include, path
admin.autodiscover()
# import the view module 
from . import views
urlpatterns = [
    path("", views.form_todo, name="formtodoapp")
]