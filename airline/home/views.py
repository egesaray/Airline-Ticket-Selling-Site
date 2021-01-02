from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as dj_login
from .forms import RegistrationForm
from home.models import RegisteredUser, User
from django.contrib import messages
from .forms import *

# Create your views here.


def home(request):
    return render(request, 'home/home.html')
def loginView(request):
    context ={}
    return render(request, 'registration/login.html',context)
def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST['username']
            password = request.POST['password1']
            user = authenticate(request, username=username, password=password)
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            phone = request.POST['phone']
            email = request.POST['email']

            values = {
                'first_name': first_name,
                'last_name': last_name,
                'phone': phone,
                'email': email,
                'user': user
            }

            registereduser = RegisteredUser(first_name=first_name,last_name=last_name, phone=phone, email=email, user=user )
            registereduser.save()
            dj_login(request, user)
            return redirect('login')  # redirect user to login page when account creation is successfull
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required
def homepage(request):
    return render(request, 'home/homepage.html')
def footer(request):
    return render(request, 'home/footer.html')
def header(request):
    return render(request, 'home/header.html')


@login_required
def changeEmail(request):
    registereduser = request.user.registereduser
    form = ChangeEmailForm(instance=registereduser)

    if request.method =='POST':
        form = ChangeEmailForm(request.POST,instance=registereduser)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'home/changeEmail.html', context)


@login_required
def changePassword(request):
    return render(request, 'home/changePassword.html')
@login_required
def creditcards(request):
    return render(request, 'home/creditcards.html')
@login_required
def logout(request):
    return render(request, 'home/logout.html')
@login_required
def myflights(request):
    return render(request, 'home/myflights.html')
@login_required
def ticket(request):
    return render(request, 'home/ticket.html')
def contactus(request):
    return render(request, 'home/contactus.html')
def aboutus(request):
    return render(request, 'home/aboutus.html')
def navbar(request):
    return render(request, 'home/navbar.html')
@login_required
def checkin(request):
    return render(request, 'home/checkin.html')
@login_required
def Feedback(request):
    return render(request, 'home/Feedback.html')
@login_required
def buyticket(request):
    return render(request, 'home/buyticket.html')
@login_required
def chooseclass(request):
    return render(request, 'home/chooseclass.html')
@login_required
def forgotPassword(request):
    return render(request, 'home/forgotPassword.html')



