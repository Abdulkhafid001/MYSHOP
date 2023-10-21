from django.contrib import admin
from django.urls import include, path
admin.autodiscover()
# import the view module 
from . import views
urlpatterns = [
    path("", views.form_todo, name="formtodoapphomepage"),
    # path("login/", views.login, name="login"),
    # path("logout", views.logout, name="logout")
    # url routing for my form view
    path('form/', views.get_name, name='viewforform'),
    # url routing for my contact form view
    path('contact/', views.get_contact_form, name='viewforcontactform')
]