# import the path fucntion to map urls to views
from django.urls import path
# import view module to invoke functions of view
from . import views
urlpatterns = [
    path('', views.test, name="testview")
]