from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.utils import timezone
import datetime
from datetime import timedelta
from .decorators import unauthenticated_user
from .forms import *
from .models import *
from django.contrib.auth import update_session_auth_hash
from .filters import *
# Create your views here.

@unauthenticated_user
def home(request):
    return render(request, 'home/home.html')

@unauthenticated_user
def loginView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password1')
        user = authenticate(request, username=username, password1=password)#databsede olup olmadığını kontrol etmek için
        if username is not None:
            login(request, user)
            return redirect('home.html')
        else:
            messages.info(request, 'Username OR password is incorrect')
    context ={}
    return render(request, 'registration/login.html',context)

@unauthenticated_user
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
            registereduser = RegisteredUser(first_name=first_name, last_name=last_name, phone=phone, email=email,user=user, my_points=0)
            registereduser.save()

            new_user_type = user_type(registereduser=registereduser, user_type='U')
            new_user_type.save()

            messages.success(request, 'Account was created for ' + username)
            return redirect('login')  # redirect user to login page when account creation is successfull
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})



@login_required
def logout(request):
    return render(request, 'home/logout.html')

@login_required
def navbar(request):
    user = request.user
    registereduser = RegisteredUser.objects.get(user=user)
    requested_user_type = user_type.objects.get(registereduser=registereduser)
    return render(request, 'home/homepage.html',{'requested_user_type': requested_user_type})


@login_required
def homepage(request):
    user = request.user
    registereduser = RegisteredUser.objects.get(user=user)
    requested_user_type = user_type.objects.get(registereduser=registereduser)
    flights = Flight.objects.filter(departure_time__range=[timezone.now(), "2022-01-01"])
    myFilter = FlightFilter(request.GET , queryset=flights)
    flights = myFilter.qs

    form = addflight()
    if request.method == "POST":
        form = addflight(request.POST)
        if form.is_valid():
            form.save()
            # for koltuk_numarasi in range(0, 3):
            #     s=seat(flight=form.flight_id, "A"koltuk_numarasi, N, first)
            #     s.save()
            #
            # for koltuk_numarasi in range(0, 3):
            #     new object(form.flight_id, B + koltuk_numarasi, N, first)
            #
            # for koltuk_numarasi in range(0, 2):
            #     new object(form.flight_id, C + koltuk_numarasi, N, business)
            # return


            return HttpResponseRedirect('/homepage/')

    if requested_user_type.user_type == 'A':
        return render(request, 'home/homepage.html', {'form':form, 'requested_user_type': requested_user_type, 'flights': flights})


    return render(request, 'home/homepage.html', {'flights': flights , 'myFilter':myFilter})


@login_required
def FeedbackPage(request):
    ruser = request.user.registereduser
    feedbackresponse = Feedback.objects.filter(registereduser=ruser)
    form = ContactForm()

    if request.method =='POST':
        form =ContactForm(request.POST)
        typer = request.POST.get('type')
        textr = request.POST.get('text')

        new_feedback = Feedback(type=typer, text=textr, registereduser=ruser , is_ok='NO')
        new_feedback.save()
        return redirect('/homepage')


    context = {'form': form, 'ruser': ruser, 'feedbackresponse': feedbackresponse}
    return render(request, 'home/Feedback.html', context)

@login_required
def feedbacklist(request):
    user = request.user
    registereduser = RegisteredUser.objects.get(user=user)
    requested_user_type = user_type.objects.get(registereduser=registereduser)
    feedbacks = Feedback.objects.filter(is_ok='NO')
    return render(request, 'home/feedbacklist.html', { 'feedbacks': feedbacks , 'requested_user_type':requested_user_type })


@login_required
def response_feedback(request , id):
    user = request.user
    registereduser = RegisteredUser.objects.get(user=user)
    requested_user_type = user_type.objects.get(registereduser=registereduser)
    firstfeedback = Feedback.objects.get(id=id)

    form = ResponseForm(request.POST, instance=firstfeedback)
    if request.method == "POST":
        if form.is_valid():
            form = ResponseForm(request.POST , instance=firstfeedback)
            form.save()
            Feedback.objects.filter(id=id).update(is_ok='YES')
            return HttpResponseRedirect('/feedbacklist')

    return render(request, 'home/response_feedback.html', {'form': form, 'requested_user_type': requested_user_type , 'firstfeedback': firstfeedback})





@login_required
def cancel_flight(request , id):
    Flight.objects.get(id=id).delete()
    return redirect('/homepage')


@login_required
def addairport(request):
    user = request.user
    registereduser = RegisteredUser.objects.get(user=user)
    requested_user_type = user_type.objects.get(registereduser=registereduser)
    form = addAirport()
    if request.method == "POST":
        form = addAirport(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/homepage/')
    return render(request, 'home/addairport.html', {'form':form,'requested_user_type': requested_user_type})



@login_required
def changeEmail(request):
    registereduser = request.user.registereduser
    form = ChangeEmailForm(instance=registereduser)

    if request.method =='POST':
        form = ChangeEmailForm(request.POST,instance=registereduser)
        if form.is_valid():
            form.save()
            return redirect('/homepage')
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
    return render(request, 'home/changePassword.html', context)

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
            expirationmonth = request.POST['expirationmonth']
            expirationyear = request.POST['expirationyear']
            cvv = request.POST['cvv']
            cardHolderName = request.POST['cardHolderName']

            credit_card = CreditCard(cardName=cardName,cardNumber=cardNumber,expirationmonth=expirationmonth,
                                     expirationyear=expirationyear,cvv=cvv,cardHolderName=cardHolderName, registereduser=ruser)
            credit_card.save()
            return HttpResponseRedirect('/creditcards/')

    context= {'mycreditcards':mycreditcards , 'form':form}
    return render(request, 'home/creditcards.html',context)




@login_required
def delete_creditcard(request,pk):
    mycreditcard = CreditCard.objects.get(id=pk)
    if request.method =="POST":
        mycreditcard.delete()
        return redirect('/creditcards')
    context= {'mycreditcard':mycreditcard}
    return render(request, 'home/delete_creditcard.html',context)

@login_required
def delete_ticket(request,pk):
    ticket = Ticket.objects.get(id=pk)
    if request.method =="POST":
        ticket.delete()
        return redirect('/myflights')
    context= {'ticket':ticket}
    return render(request, 'home/delete_ticket.html',context)

@login_required
def cancel_ticket(request , id):
    Ticket.objects.get(id=id).delete()
    return redirect('/myflights')

@login_required
def myflights(request):
    user_id = request.user.id
    user = User.objects.get(id=user_id)
    registered_user = RegisteredUser.objects.get(user=user)
    my_tickets = Ticket.objects.filter(registereduser=registered_user)


    get_datetime_now = str(datetime.datetime.now()).split(' ')
    get_date_now = str(get_datetime_now[0]).split('-')
    year = get_date_now[0]
    month = get_date_now[1]
    day = get_date_now[2]


    past_flights = []
    incoming_flights = []


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
def checkin(request):

    user_id = request.user.id
    user = User.objects.get(id=user_id)
    registered_user = RegisteredUser.objects.get(user=user)
    my_tickets = Ticket.objects.filter(registereduser=registered_user)


    incoming_flights = []


    for ticket in my_tickets:
        flight = ticket.flight
        deparature_date = datetime.datetime.strptime(str(flight.departure_time) + ' ' + str(flight.departure_hour), '%Y-%m-%d %H:%M:%S')
        get_datetime_yesterday = deparature_date - datetime.timedelta(days=1)
        if datetime.datetime.now() > get_datetime_yesterday and datetime.datetime.now() < deparature_date and ticket.is_checkin == False:
                incoming_flights.append(ticket)


    Ticket.objects.filter(registereduser=registered_user, flight=flight).update(is_checkin=True)


    return render(request, 'home/checkin.html', {'incoming_flights': incoming_flights})

@login_required
def buyticket(request,values):

    Arow = request.POST.get('Arow')
    Acolumn = request.POST.get('Acolumn')
    selectedseats = str(Arow) + "-" + str(Acolumn)


    values = str(values).split('&')
    try:
        flight_class = values[0]
        flight_id = values[1]
        choices = values[2]
    except:
        return HttpResponse("Invalid request")


    values_of_choices = str(choices).split('_')
    kid = int(values_of_choices[1])
    adult = int(values_of_choices[2])
    senior = int(values_of_choices[3])


    flight = Flight.objects.get(id=flight_id)
    price = flight.price

    kid_price = int(price / 3)
    adult_price = int(price)
    senior_price = int(price / 2)


    user_id = request.user.id
    user = User.objects.get(id=user_id)
    registered_user = RegisteredUser.objects.get(user=user)


    # aynisi aslinda
    # registered_user = RegisteredUser.objects.get(user=request.user.id)

    #saved cards
    # mycreditcards = registered_user.creditcard_set.all
    mycreditcards = request.user.registereduser.creditcard_set.all()



    # to store total price
    ticket_price = 0
    if flight_class.__eq__("economy"):
        ticket_price = ticket_price + (kid_price * kid) + (adult_price * adult) + (senior_price * senior)
    elif flight_class.__eq__("business"):
        ticket_price = ticket_price + ((kid_price * kid) + (29 * kid)) + ((adult_price * adult) + (29 * adult)) + ((senior_price * senior) + (29 * senior))
    elif flight_class.__eq__("first"):
        ticket_price = ticket_price + ((kid_price * kid) + (59 * kid)) + ((adult_price * adult) + (59 * adult)) + ((senior_price * senior) + (59 * senior))
    else:
        return HttpResponse("Invalid request")

    # kredi karti onayindan sonra...
    ticket = Ticket(is_checkin=False,trip='o',seat=selectedseats , registereduser=registered_user, ticket_class=flight_class, flight=flight, ticket_price=ticket_price, created_at=timezone.now(), is_approval='F')
    ticket.save()


    my_points = request.user.registereduser.my_points

    if (price > 0):
        total_point = (float(my_points) + float((ticket.ticket_price *5)/100))

    RegisteredUser.objects.filter(id=user_id).update(my_points=total_point)
    return render(request, 'home/buyticket.html', {'ticket':ticket ,'mycreditcards':mycreditcards, 'my_points':my_points})



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
    seray = Ticket.objects.get(id=id)

    point = request.POST.get('point')
    if not point=="-99":
        user_id = request.user.id
        user = User.objects.get(id=user_id)
        registered_user = RegisteredUser.objects.get(user=user)
        my_points = request.user.registereduser.my_points
        ticket_price = seray.ticket_price
        total_point = (float(ticket_price) - float(my_points))
        RegisteredUser.objects.filter(user=user).update(my_points=0)
        Ticket.objects.filter(registereduser=registered_user).update(ticket_price=total_point)  # id eşitlicez
        seray2=float((total_point*5)/100)
        RegisteredUser.objects.filter(user=user).update(my_points=seray2)

    if point=="-99":
        user_id = request.user.id
        user = User.objects.get(id=user_id)
        my_points = request.user.registereduser.my_points
        ticket_price = seray.ticket_price
        seray2 = (float(my_points) + float(( ticket_price* 5) / 100))
        RegisteredUser.objects.filter(user=user).update(my_points=seray2)
        registered_user = RegisteredUser.objects.get(user=user)


    Ticket.objects.filter(id=id).update(is_approval='T')
    return redirect('/completed')

@login_required
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
    ruser = request.user.registereduser
    namee= str(ruser.first_name) + " " + str(ruser.last_name)
    return render(request , 'home/view_ticket.html',{'ticket':ticket , 'namee':namee })



@login_required
def ChooseSeat(request, values):
    vals= values
    values = str(values).split('&')
    flight_class = values[0]
    flight_id = values[1]
    choices = values[2]
    values_of_choices = str(choices).split('_')
    kid = int(values_of_choices[1])
    adult = int(values_of_choices[2])
    senior = int(values_of_choices[3])

    total = kid+adult+senior

    count = []
    for i in range(0,total):
        count.append(i)

    return render(request,'home/ChooseSeat.html' ,  {'vals':vals ,'count':count, 'flight_class':flight_class })


