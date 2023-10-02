# the objective is to map our view to a http request
from django.urls import path

from votingapp import views

urlpatterns = [
    # map app root view to a url
    path("", views.appindex, name="index"),
]