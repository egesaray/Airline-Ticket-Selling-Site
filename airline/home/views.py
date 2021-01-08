from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.forms import UserCreationForm , PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as dj_login
from django.contrib.auth import update_session_auth_hash
from .forms import RegistrationForm
from home.models import RegisteredUser, User
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from django.utils import timezone
import datetime
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
    form = PasswordChangeForm(data=request.POST, user=request.user)
    if request.method =='POST':
        form = PasswordChangeForm(data=request.POST,user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user) # değiştirdikten sonra hala giriş yapmış şekilde kalması için
            return redirect('/homepage')
    context = {'form':form}
    return render(request, 'home/changePassword.html',context)

@login_required
def creditcards(request):
    mycreditcards = request.user.registereduser.creditcard_set.all()
    ruser = request.user.registereduser

    form = AddCreditCardForm(request.POST)
    if request.method =='POST':
        if form.is_valid():
            form =AddCreditCardForm(request.POST)
            cardName = request.POST['cardName']
            cardNumber = request.POST['cardNumber']
            expiration = request.POST['expiration']
            cvv = request.POST['cvv']
            cardHolderName = request.POST['cardHolderName']

            credit_card = CreditCard(cardName=cardName,cardNumber=cardNumber,expiration=expiration,
                                     cvv=cvv,cardHolderName=cardHolderName, registereduser=ruser)
            credit_card.save()


    context= {'mycreditcards':mycreditcards , 'form':form}
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
    context= {'mycreditcard':mycreditcard}
    return render(request, 'home/delete_creditcard.html',context)


@login_required
def logout(request):
    return render(request, 'home/logout.html')


@login_required
def myflights(request):

    # to find critical information
    user_id = request.user.id
    user = User.objects.get(id=user_id)
    registered_user = RegisteredUser.objects.get(user=user)
    my_tickets = Ticket.objects.filter(registereduser=registered_user)

    # brute force approach to get the current date
    get_datetime_now = str(datetime.datetime.now()).split(' ')
    get_date_now = str(get_datetime_now[0]).split('-')
    year = get_date_now[0]
    month = get_date_now[1]
    day = get_date_now[2]

    # to return values
    past_flights = []
    incoming_flights = []


    # to detect past and next
    for ticket in my_tickets:
        flight = ticket.flight

        departure_time = str(flight.departure_time).split('-')
        departure_time_year = departure_time[0]
        departure_time_month = departure_time[1]
        departure_time_day = departure_time[2]

        if int(departure_time_year) < int(year) \
                or (int(departure_time_year).__eq__(int(year)) and int(departure_time_month) < int(month)) \
                or (int(departure_time_year).__eq__(int(year)) and int(departure_time_month).__eq__(int(month)) and int(departure_time_day) < int(day)):
            past_flights.append(ticket)
        else:
            incoming_flights.append(ticket)

    return render(request, 'home/myflights.html', {'past_flights' : past_flights, 'incoming_flights' : incoming_flights})


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
def buyticket(request,values):
    # to get critical values from url
    values = str(values).split('&')
    try:
        flight_class = values[0]
        flight_id = values[1]
        choices = values[2]
    except:
        return HttpResponse("Invalid request")

    # kid-adult-senior
    values_of_choices = str(choices).split('_')
    kid = int(values_of_choices[1])
    adult = int(values_of_choices[2])
    senior = int(values_of_choices[3])

    # flight information
    flight = Flight.objects.get(id=flight_id)
    price = flight.price

    # will be used for calculations per a ticket
    kid_price = int(price / 3)
    adult_price = int(price)
    senior_price = int(price / 2)

    # to find the registered user using user that makes request
    user_id = request.user.id
    user = User.objects.get(id=user_id)
    registered_user = RegisteredUser.objects.get(user=user)

    # aynisi aslinda
    # registered_user = RegisteredUser.objects.get(user=request.user.id)

    # to store total price
    ticket_price = 0
    if flight_class.__eq__("economy"):
        ticket_price = ticket_price + (kid_price * kid) + (adult_price * adult) + (senior_price * senior)
    elif flight_class.__eq__("business"):
        ticket_price = ticket_price + (kid_price * kid) + (adult_price * adult) + (senior_price * senior) + 29
    elif flight_class.__eq__("first"):
        ticket_price = ticket_price + (kid_price * kid) + (adult_price * adult) + (senior_price * senior) + 59
    else:
        return HttpResponse("Invalid request")

    # kredi karti onayindan sonra...
    ticket = Ticket(trip='o', registereduser=registered_user, ticket_class=flight_class, flight=flight, ticket_price=ticket_price, created_at=timezone.now(), is_approval='F')
    ticket.save(force_insert=True)

    return render(request, 'home/buyticket.html', {'ticket':ticket})

@login_required
def choose_class(request, id):
    url = 'home/chooseclass.html'
    context = Flight.objects.get(id=id)
    kid = request.POST.get('kid')
    adult = request.POST.get('adult')
    senior = request.POST.get('senior')
    choices = "ch_" + str(kid) + "_" + str(adult) + "_" + str(senior)
    return render(request,url,{'context':context, 'choices' : choices})

@login_required
def ticket_has_been_purchased(request, id):
    Ticket.objects.filter(id=id).update(is_approval='T')
    return redirect('/completed')

def completed(request):
    return render(request, 'home/completed.html')

@login_required
def selected_flight(request, flight_id):
    url = 'home/selected_flight.html'
    flight = Flight.objects.get(id=flight_id)
    return render(request, url, {'flight': flight})

@login_required
def view_ticket(request, id):
    ticket = Ticket.objects.get(id=id)
    return render(request , 'home/view_ticket.html',{'ticket':ticket})

def cancel_ticket(request , id):
    Ticket.objects.get(id=id).delete()
    return redirect('/myflights')

@login_required
def forgotPassword(request):
    return render(request, 'home/forgotPassword.html')



