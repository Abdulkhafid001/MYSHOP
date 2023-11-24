from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
admin.autodiscover()

urlpatterns = [
    # register the jerseystore URLConf
    path('',include('jerseystore.urls')),
    # register the blog app URLConf
    path('blog/', include('blog.urls')),
    # register weather app URLConf
    path('weatherapp/', include('myweather.urls')),
    # register todo form app URLConf
    path('todoapp/', include('formtodo.urls')),
    # register the todolist app URLConf which serves as a link to the app
    path('todolist/', include('todolist.urls')),
    # register the aptech team URLConf
    path('aptechteam/', include('aptechteam.urls')),
    # this file serves as the parent URLConf of the project therefore all apps URLConf must be registered here
    path('mainpollapp/', include('mainpollapp.urls')),
    # here we import the votingapp as a high-level app in our parent mysite project
    # add the URLConf of my voting app to the main project
    # Define a pattern for the root path
    path('votingapp/', include('votingapp.urls')),
    # here we import the polls app as a high-level app in our parent mysite project
    # path('', include('polls.urls')),  # Define a pattern for the root path
    path('admin/', admin.site.urls),
    # add django-debug-toolbar URL to your project URLConf
    path("__debug__/", include("debug_toolbar.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
