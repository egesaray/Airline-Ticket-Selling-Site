from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.

def home(request):
    return render(request, 'home/main.html')
def login(request):
    return render(request, 'home/login.html')
def register(request):
    return render(request, 'home/register.html')
def homepage(request):
    return render(request, 'home/homepage.html')


