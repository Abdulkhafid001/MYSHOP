from django.shortcuts import render, redirect
# login and logout users using the django authenticate framework
# step1: import the modules for the user login/logout
from django.contrib.auth import authenticate, login, logout
# we want to display messages using django
from django.contrib import messages

# Create your views here.


def form_todo(request):
    # step 3: here we get parameters from the form
    # i. check if the user is trying to log in by checking the request method
    if request.method == 'post':
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
