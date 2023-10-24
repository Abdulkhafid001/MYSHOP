from django import forms
from django.forms import ModelForm
from formtodo.models import Customer, TodoList


class NameForm(forms.Form):
    your_name = forms.CharField(label="Your name", max_length=100)
    your_age = forms.CharField(label="enterPassword", max_length=12)

    def __str__(self):
        return self.your_name + " " + self.your_age


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)

    def __str__(self):
        return self.subject + " " + self.sender

# implementing the modelform concept
# step 1: create a that derives from model form


class CustomerForm(ModelForm):
    # step2: create a meta class that serves as a detail to set model info
    class Meta:
        model = Customer
        fields = '__all__'


class TodolistForm(ModelForm):
    class Meta:
        model = TodoList
        fields = '__all__'
