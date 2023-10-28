from django.http import HttpResponseRedirect
# import the class in the form module
from .forms import NameForm, ContactForm, CustomerForm, TodolistForm
from django.shortcuts import render, redirect
# login and logout users using the django authenticate framework
# step1: import the modules for the user login/logout
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# import email classes
from django.core.mail import send_mail
# import model into view module to use the model
from formtodo.models import Customer, TodoList
# Create your views here.


def form_todo(request):
    # step 3: here we get parameters from the form
    # i. check if the user is trying to log in by checking the request method
    if request.method == '':
        # get the parameters
        username = request.POST['username']
        password = request.POST['password']
        # authenticate the user check if he/she exists
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # show a welcome message
            messages.success(request, "welcome to the app")
            # redirect to homepage
            return redirect(request, 'formtodoapphomepage')
        else:
            # show an error message to user if login failed
            messages.success("There was an error, Please try again...")
            # and redirect to homepage
            return redirect(request, 'formtodoapphomepage')
    # template = loader.get_template("index.html")
    return render(request, "homepage.html")

# step 2 create views to handle the login and logout
# use this when i need a separate login page
# def login_user(request):
#     pass


def logout_user(request):
    pass


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect("/formtodoapphomepage/")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, "name.html", {"form": form})
# implementing view for contact form


def get_contact_form(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        contact_form = ContactForm(request.POST)
        # check whether it's valid:
        if contact_form.is_valid():
            # process the data in form.cleaned_data as required
            # when the condition passes we can get cleaned data from the cleaned data dictionary
            subject = contact_form.cleaned_data["subject"]
            message = contact_form.cleaned_data["message"]
            sender = contact_form.cleaned_data["sender"]
            cc_myself = contact_form.cleaned_data["cc_myself"]
            # send myself an email using the contact form field data
            # step 1: import the relevent classes for email
            # step 2: create a recipient
            recipients = ["kabiruabdulkhafid@gmail.com"]
            # if user click on send then add username
            if cc_myself:
                recipients.append(sender)

            send_mail(subject, message, sender, recipients)
            # redirect to a new URL:
            return HttpResponseRedirect("/formtodoapphomepage/")

    # if a GET (or any other method) we'll create a blank form
    else:
        # if get or other method just create a form by instantiating the ContactForm class.
        contact_form = ContactForm()

    return render(request, "contact.html", {"contactForm": contact_form})
# task: create a view that handles modelform which get form data and add it to a priority queue depending on task stage


def handle_model_form(request):
    # instantiate our CustomerForm
    customer_form = CustomerForm()
    if request.method == 'POST':
        # check if form that has been retreived
        print(request.POST)
        # since we use the method above to get all the form data we could also use it to pass all our form data into our model
        customer_form = CustomerForm(request.POST)
        # validate the form data
        if customer_form.is_valid():
            # save the object
            customer_form.save()

    # now get all customers from the database
    all_customers = Customer.objects.all()
    context = {'customerForm': customer_form, 'ourCustomers': all_customers}
    return render(request, 'contact.html', context)


def handle_todolist_form(request):
    if request.method == 'POST':
        todolist_form = TodolistForm(request.POST)
        if todolist_form.is_valid():
            todolist_form.save()
    else:
        todolist_form = TodolistForm()

    # now get all customers from the database
    all_tasks = TodoList.objects.all()
    # create a context with database content and modelform
    context = {'userTasks': all_tasks, 'todolistForm': TodolistForm}
    return render(request, 'homepage.html', context)
