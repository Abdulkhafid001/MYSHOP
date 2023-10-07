from django.shortcuts import render
from django.http import HttpResponse
# import all app models
from .models import CandidateInfo, ElectionResult
# Create your views here.


def indexView(request):
    # from my index view i would get candidate info using a dictionary as a context
    # get all the values from the table
    table_content = CandidateInfo.objects.all().values()
    return render(request, "index.html", {"candidate": table_content})
