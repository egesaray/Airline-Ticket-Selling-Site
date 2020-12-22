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
def footer(request):
    return render(request, 'home/footer.html')
def header(request):
    return render(request, 'home/header.html')
def changeEmail(request):
    return render(request, 'home/changeEmail.html')
def changePassword(request):
    return render(request, 'home/changePassword.html')
def creditcards(request):
    return render(request, 'home/creditcards.html')
def logout(request):
    return render(request, 'home/logout.html')
def myflights(request):
    return render(request, 'home/myflights.html')
def ticket(request):
    return render(request, 'home/ticket.html')
def contactus(request):
    return render(request, 'home/contactus.html')
def aboutus(request):
    return render(request, 'home/aboutus.html')
def navbar(request):
    return render(request, 'home/navbar.html')
def checkin(request):
    return render(request, 'home/checkin.html')
def Feedback(request):
    return render(request, 'home/Feedback.html')
def buyticket(request):
    return render(request, 'home/buyticket.html')
def chooseclass(request):
    return render(request, 'home/chooseclass.html')
def forgotPassword(request):
    return render(request, 'home/forgotPassword.html')



