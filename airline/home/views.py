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
from .models import *

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
    flights = Flight.objects.all()
    context = {'flights': flights}

    return render(request, 'home/homepage.html', context)
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
    mycreditcards = request.user.registereduser.creditcard_set.all()#set sil
    form = AddCreditCardForm(request.POST)
    if request.method =='POST':
        if form.is_valid():
            form =AddCreditCardForm(request.POST)
            form.save()

    context= {'mycreditcards':mycreditcards , 'form':form }
    return render(request, 'home/creditcards.html',context)


@login_required
def Feedback(request):
    form = ContactForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form = ContactForm(request.POST)
            form.save()
    context = {'form': form}
    return render(request, 'home/Feedback.html', context)


@login_required
def delete_creditcard(request,pk):
    mycreditcard = CreditCard.objects.get(id=pk)
    if request.method =="POST":
        mycreditcard.delete()
        return redirect('/creditcards')
    context= {'mycreditcard':mycreditcard }
    return render(request, 'home/delete_creditcard.html',context)







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
def checkin(request,flight_class): #if içinde cls==economy cls==business+30..

    return render(request, 'home/checkin.html')




@login_required
def buyticket(request):
    return render(request, 'home/buyticket.html')

@login_required
def chooseclass(request, id):
    url = 'home/chooseclass.html'
    context = Ticket.objects.get(id=id)
    price = context.price
    return render(request,url,{'context':context})


@login_required
def forgotPassword(request):
    return render(request, 'home/forgotPassword.html')



