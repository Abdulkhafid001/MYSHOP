# the objective is to map our view to a http request
from django.urls import path
#import the view module inorder to call the functions
from polls import views

urlpatterns = [
    path("", views.index, name="index"),
    # creating a new path for my view
    path("myview/", views.my_view, name="my_view"),
    # creating a new path for my view 2
    path("myview2/", views.view2, name="my_view"),
    # creating a view for new way to write 
    path("helloview/", views.hello, name="helloview"),
    # now to map a url to a full html page from our folder.
    path("vote", views.vote, name="abdulkhafidvoteview"),
    # path for my todo template
    path("todo", views.todoapp, name="todos"),
]
