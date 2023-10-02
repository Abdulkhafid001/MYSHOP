# the objective is to map our view to a http request
from django.urls import path

from votingapp import views

urlpatterns = [
    # map app root view to a url
    path("", views.appindex, name="index"),
    # ex: /polls/5/
    path("<int:question_id>/", views.detail, name="detail"),
    # ex: /polls/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
]