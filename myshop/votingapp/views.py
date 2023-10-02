from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.
# this view serves as a root path for my project in the app


def appindex(request):
    return HttpResponse("<h1>voting app root path</h1>")
# this views are to get,show and vote they cover all the app functionality


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
