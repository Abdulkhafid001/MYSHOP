# import the path module
from django.urls import path

# import our view module
from mainpollapp import views
urlpatterns = [
    path('', views.indexView, name="pollingapphomepage")
]