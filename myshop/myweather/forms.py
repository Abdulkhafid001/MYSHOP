from django.forms import ModelForm
from django import forms
from .models import Userweather

# create a class that derives from the ModelForm class


class UserInput(ModelForm):
    # step2: create a meta class that serves as a detail to set model info
    class Meta:
        model = Userweather
        fields = '__all__'
