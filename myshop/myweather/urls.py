# import the views.py module in order to call the view functions
from myweather import views
# import the admin panel to call the function of the class
from django.contrib import admin
# import url routing library
from django.urls import path
# invoke autodiscover method
admin.autodiscover()
# creat urlpattern list
urlpatterns = [
    path("", views.get_api_data, name="weatherview")
]