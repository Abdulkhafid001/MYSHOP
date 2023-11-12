from blog import views
from django.contrib import admin
from django.urls import path
admin.autodiscover()
urlpatterns = [
    path('', views.say_hello, name='blogapphome')
]