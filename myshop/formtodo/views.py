from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

# Create your views here.
def form_todo(request):
    # template = loader.get_template("index.html")
    return render(request, "homepage.html")