from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from .models import *
from django.utils.translation import ugettext_lazy as _

# Create your models here.


class RegisteredUser(models.Model):
    user= models.OneToOneField(User,null=True,on_delete=models.CASCADE)   ## realation with django's user
    first_name = models.CharField(max_length=255,null=True)
    last_name = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=11, null=True)
    email = models.EmailField(max_length=254)
    date_created = models.DateField(auto_now_add=True,null=True)
    my_points = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    def __str__(self):
        return self.first_name+" "+self.last_name
    
    def register(self):
        return self.save()


class CreditCard(models.Model):
    expmonth = (
        ('01', '01'),
        ('02', '02'),
        ('03', '03'),
        ('04', '04'),
        ('05', '05'),
        ('06', '06'),
        ('07', '07'),
        ('08', '08'),
        ('09', '09'),
        ('10', '10'),
        ('11', '11'),
        ('12', '12'),
    )
    expyear = (
        ('21', '21'),
        ('22', '22'),
        ('23', '23'),
        ('24', '24'),
        ('25', '25'),
        ('26', '26'),
        ('27', '27'),
        ('28', '28'),
        ('29', '29'),
    )
    cardNumber= models.DecimalField(max_digits=16,decimal_places=0, null=True)
    cardName= models.CharField(max_length=255,null=True)
    expirationmonth = models.CharField(max_length=2,null=True, blank=False, choices=expmonth)
    expirationyear = models.CharField(max_length=2,null=True, blank=False ,choices=expyear)
    cvv = models.DecimalField(max_digits=3,decimal_places=0,null=True)
    cardHolderName = models.CharField(max_length=255,null=True)
    registereduser =models.ForeignKey(RegisteredUser,null=True,on_delete= models.CASCADE)

    def __str__(self):
        return self.cardName

    def creditcards(self):
        return self.save()


class Feedback(models.Model):
    TYPE = (
        ('request','request'),
        ('suggestion','suggestion'),
        ('complaint','complaint')
    )
    ISOK =(
        ('YES','YES'),
        ('NO','NO')
    )
    type= models.CharField(max_length=255,null=True,choices=TYPE)
    text= models.TextField(max_length=1000, null=True)
    registereduser =models.ForeignKey(RegisteredUser,null=True,on_delete= models.CASCADE)
    adminresponse=models.TextField(max_length=1000,null=True,blank=True)
    is_ok = models.CharField(default='NO', max_length=10, null=True , choices=ISOK)


    def __str__(self):
        return str(self.id)


class Airport(models.Model):
    name=models.CharField(max_length=255,null=True)
    address=models.CharField(max_length=500,null=True)

    def __str__(self):
        return self.name


class Flight(models.Model):
    pnr=models.CharField(max_length=10, null=True)
    departure_time = models.DateField(auto_now_add=False, auto_now=False, null=True)
    arrival_time = models.DateField(auto_now_add=False, auto_now=False, null=True)
    departure_hour=models.TimeField(auto_now=False, auto_now_add=False, null=True)
    arrival_hour = models.TimeField(auto_now=False, auto_now_add=False, null=True)
    from_airport = models.ForeignKey(Airport, null=True,on_delete=models.SET_NULL, related_name="from_airport")
    to_airport = models.ForeignKey(Airport, null=True,on_delete=models.SET_NULL, related_name="to_airport")
    price= models.DecimalField(max_digits=10,decimal_places=2,null=True)

    def __str__(self):
        return self.pnr

    def get_departure_time(self):
        return self.departure_time


class Ticket(models.Model):
    trip_choice = (('o','oneway'),('r','roundtrip'),)
    trip = models.CharField(max_length=5, choices=trip_choice)
    seat = models.CharField(max_length=255,null=True)
    registereduser =models.ForeignKey(RegisteredUser,null=True,on_delete= models.CASCADE)
    ticket_class = models.CharField(max_length=255,null=True)
    flight = models.ForeignKey(Flight,null=True,on_delete=models.CASCADE)
    ticket_price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    created_at = models.CharField(max_length=255,null=True)
    is_approval = models.CharField(max_length=1, null=True)
    is_checkin = models.BooleanField(null=True, blank=True)


    def __str__(self):
        return str(self.id) + " - " + str(self.registereduser.first_name) + " " + str(self.registereduser.last_name)

    def chooseclass(self):
        return self.save()

class seat(models.Model):
    seat = models.CharField(max_length=255,null=True)
    flight = models.ForeignKey(Flight, null=True, on_delete=models.CASCADE)
    is_sold = models.CharField(max_length=1, null=True, default='N')
    flightclass = models.CharField(max_length=255,null=True)

class user_type(models.Model):
    registereduser = models.ForeignKey(RegisteredUser, on_delete=models.SET_NULL, null=True)
    user_type_choice = (('A', 'Admin'), ('U', 'User'))
    user_type = models.CharField(choices=user_type_choice, max_length=100, null=True)

    def __str__(self):
        return str(self.registereduser.first_name) + ' ' + str(self.registereduser.last_name) + ' (' + str(self.user_type) + ')'

    class Meta:
        verbose_name = 'User Type'
        verbose_name_plural = 'User Types'
        ordering = ['user_type']