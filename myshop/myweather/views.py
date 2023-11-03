from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from django.core import serializers
# import modelform class
from .forms import UserInput
# import the installed requests API
import requests
# Create your views here.
from .models import Student


def show_weather(request):
    # this method gets all the model objects
    data = list(Student.objects.values())
    # using the serializer to serialize the model data
    db_objects = serializers.serialize('json', Student.objects.all())
    return HttpResponse(db_objects, content_type='application/json')


# the function gets the openweather map api data by using python requests api
def get_api_data(request):

    if request.method == 'POST':
        # instantiate the form class
        weatherapp_form = UserInput(request.POST)
        if weatherapp_form.is_valid:
            # save form data to model
            weatherapp_form.save()
        else:
            #  just instantiate the form
            weatherapp_form = UserInput()
        # get the location, lat, lon
        location = weatherapp_form.cleaned_data["city"]
        lat = weatherapp_form.cleaned_data["lat"]
        lon = weatherapp_form.cleaned_data["lon"]
        # logic to get userdata from the weather API
        api_key = '3f365be1c47d424ba41193728232910'
        url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={location}'
        # Now, you can use the 'url' variable to make an API request to OpenWeatherMap's One Call API using your variables.
        api_response = requests.get(url=url).json()
        return render(request, "index.html", [{'weatherdata': api_response}, {'weatherForm': weatherapp_form}])
