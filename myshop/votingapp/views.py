from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.
# this view serves as a root path for my project in the app


def appindex(request):
    return HttpResponse("<h1>voting app root path</h1>")


def testView(request):
    return HttpResponse("<h1>Perfect</h1>")
