from django.shortcuts import render
from .models import TodoItem
from .models import Poll

# Create your views here.
# A view is just a Python function that will take a request and then return a response object.
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>app root path</h1>")

# create another view and map it to the url


def view2(request):
    return HttpResponse("the second view")


def my_view(request):
    return HttpResponse("<!DOCTYPE html><html lang='en'><head><meta charset='UTF-8'><meta name='viewport' content='width=device-width, initial-scale=1.0'><title>About Abdulkhafid Kabiru</title></head><body><h1>About Abdulkhafid Kabiru</h1><p>Name: Abdulkhafid Kabiru</p><p>Age: 30</p><p>Contact Information:</p><ul><li>Email: abdulkhafid@example.com</li><li>Phone: +123-456-7890</li><li>Address: 123 Main Street, Cityville, Country</li></ul></body></html>")

# there are other ways to write views


def hello(request):
    text = "<h1>New way to write a view</h1>"
    return HttpResponse(text)

# we can pass parameters to our view as such


def vote(request):
    # get all our database column values first
    result = Poll.objects.all()
    return render(request, "C:\\Users\\Lenovo yoga\\Desktop\\MYSHOP\\myshop\\polls\\templates\\index.html", {"votes": result})


def todoapp(request):
    # get all our database column values first
    items = TodoItem.objects.all()
    return render(request, "todo.html", {"todos": items})
