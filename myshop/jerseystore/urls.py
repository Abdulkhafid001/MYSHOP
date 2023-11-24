from django.urls import path
from . import views
urlpatterns = [
    path("", view=views.welcome_to_store, name="jerseystorehomepage")
]