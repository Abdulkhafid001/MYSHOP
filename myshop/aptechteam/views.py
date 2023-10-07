from django.shortcuts import render
from django.http import HttpResponse
# import my model
from .models import Members
# import template loader
from django.template import loader
# Create your views here.
def members(request):
    # indexpage = loader.get_template("allmembers.html")
    # get all the data in the model(table) 
    team_members = Members.objects.all().values()
    context = {
        # create a dictionary and store the values from the model
        "team" : team_members,
    }
    return render(request, "allmembers.html", context)