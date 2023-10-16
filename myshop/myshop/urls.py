"""
URL configuration for myshop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
admin.autodiscover()

urlpatterns = [
    # register todo form app URLConf
    path('', include('formtodo.urls')),
    # register the todolist app URLConf which serves as a link to the app
    path('todolist', include('todolist.urls')),
    # register the aptech team URLConf
    path('aptechteam', include('aptechteam.urls')),
    # this file serves as the parent URLConf of the project therefore all apps URLConf must be registered here
    path('mainpollapp/', include('mainpollapp.urls')),
    # here we import the votingapp as a high-level app in our parent mysite project
    # add the URLConf of my voting app to the main project
    path('votingapp', include('votingapp.urls')), # Define a pattern for the root path
    # here we import the polls app as a high-level app in our parent mysite project
    # path('', include('polls.urls')),  # Define a pattern for the root path
    path('admin/',admin.site.urls),
    # add django-debug-toolbar URL to your project URLConf
    path("__debug__/", include("debug_toolbar.urls")),
]
