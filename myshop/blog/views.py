from django.shortcuts import render
from django.http import HttpResponse , HttpRequest

# Create your views here.
def say_hello(request):
    return HttpResponse("<h1>Login or Signup to MyBlog</h1>")
