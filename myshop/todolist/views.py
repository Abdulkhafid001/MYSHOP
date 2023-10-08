from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
# Create your views here.
def test(request):
    return HttpResponse("<h1>todo app homepage</h1>")