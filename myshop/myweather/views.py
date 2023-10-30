from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from django.core import serializers
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


# the function gets the openweather map api data by using django request api
def get_api_data(request):
    api_key = '3f365be1c47d424ba41193728232910'
    lat = 10
    lon = 8
    date = '10/29/2023'
    # Specify the part to exclude, e.g., 'minutely' or 'hourly' or 'daily', or you can leave it out if you don't want to exclude any part.
    part = 'minutely'
    url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q=Abuja'
    # Now, you can use the 'url' variable to make an API request to OpenWeatherMap's One Call API using your variables.
    api_response = requests.get(url=url).json()
    # JsonResponse(api_response)
    return render(request, "index.html", {'weatherdata': api_response})
