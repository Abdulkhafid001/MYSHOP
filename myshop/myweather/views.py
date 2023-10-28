from django.shortcuts import render, redirect, HttpResponse
# Create your views here.


def show_weather(request):
    return HttpResponse("<h1>Welcome to the weather app.</h1>")
