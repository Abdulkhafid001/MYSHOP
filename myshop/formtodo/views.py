from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def form_todo(request):
    return HttpResponse("<h1>Home page of the form todo app.</h1>")