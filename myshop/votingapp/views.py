from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
# Create your views here.
# this view serves as a root path for my project in the app


def appindex(request):
    return HttpResponse("<h1>voting app root path</h1>")


# this views are to get,show and vote they cover all the app functionality

# this views take a parameter and pass it to the this URLConf

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
# now we want to read list of questions from our question database and display them by order of publication date
# step 1: get our question database
from .models import Question
#step 2: create a view to hold all the records in the table
def index(request):
    # get all the objects in the question database and sort them in ascending order
    latest_question_list = Question.objects.order_by("pub_date")[:5]
    # use the loader class to get the template loader
    template = loader.get_template("polls/index.html")
    # now convert our database rows into  a dictionary and pass it to the view 
    context = {
        "latest_question_list": latest_question_list,
    }
    # then covert into type httpresponse and render to the template
    return HttpResponse(template.render(context, request))
