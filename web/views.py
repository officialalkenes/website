from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def homepage(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def projects(request):
    return render(request, "projects.html")

def login(request):
    return render(request, "login.html")

def signup(request):
    return render(request, "signup.html")