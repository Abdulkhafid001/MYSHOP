from django.shortcuts import render, HttpResponse

# Create your views here.
def welcome_to_store(request):
    return render(request,'index.html')
