from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from .models import *

#İrfan Ege Saray

# Create your models here.

#Problem çıkmasını engellemek için geliştirme sürecinde hepsi null=True , son sürümde güncellenecektir.


#***********ÖNEMLİ**********
# şifrelerin gizlenmesi,authentication gibi özellikler için djangonun sağladığı userı kullanıyoruz
# ancak user ın başka şeylerle bağlantı kurması gerekiyor örneğin uçak bileti, bundan dolayı RegisteredUser tablosu oluşturuyoruz
# ve bu tablo django'nun userı ile OneToOne relation kuruyor. Bir kişi kayıt olduğunda o kişi için registeredUser tablosu oluşması gerek
# ve bunun nasıl yapılacağına dair internette kaynaklar mevcut
#***********ÖNEMLİ**********

class RegisteredUser(models.Model):

    user= models.OneToOneField(User,null=True,on_delete=models.CASCADE)   ## realation with django's user
    first_name = models.CharField(max_length=255,null=True)
    last_name = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=11, null=True)
    email = models.EmailField(max_length=254)
    date_created = models.DateField(auto_now_add=True,null=True)


    def __str__(self):
        return self.first_name+" "+self.last_name
    def register(self):
        return self.save()


class CreditCard(models.Model):
    cardNumber= models.CharField(max_length=16, null=True)
    cardName= models.CharField(max_length=255,null=True)
    expiration = models.CharField(max_length=5, null=False, blank=False)# form ile uyumsuzluk olursa integer yapılabilir
    cvv = models.CharField(max_length=3,null=True)
    cardHolderName = models.CharField(max_length=255,null=True)
    registereduser =models.ForeignKey(RegisteredUser,null=True,on_delete= models.SET_NULL)

    def __str__(self):
        return self.cardName


class Feedback(models.Model):
    TYPE = (
        ('request','request'),
        ('suggestion','suggestion'),
        ('complaint','complaint')
    )
    feedback_id = models.CharField(max_length=255,null=True)
    type= models.CharField(max_length=255,null=True,choices=TYPE)
    text= models.TextField()
    registereduser =models.ForeignKey(RegisteredUser,null=True,on_delete= models.SET_NULL)

    def __str__(self):
        return self.feedback_id


class Airport(models.Model):
    name=models.CharField(max_length=255,null=True)
    address=models.CharField(max_length=500,null=True)

    def __str__(self):
        return self.name


class Flight(models.Model):
    pnr=models.CharField(max_length=10, null=True)
    departure_time = models.DateTimeField(auto_now_add=False, auto_now=False, null=True)
    arrival_time = models.DateTimeField(auto_now_add=False, auto_now=False, null=True)
    airport = models.ForeignKey(Airport, null=True,on_delete=models.SET_NULL)  # ilk seçilen kalkış, aradakiler aktarma,son seçilen varış olabilir??!!

    def __str__(self):
        return self.pnr


class Ticketclass(models.Model):
    ticket_name = models.CharField(max_length=500, null=True)  # economy,business,first class names
    extra_price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    def __str__(self):
        return self.ticket_name


class Ticket(models.Model,):
    trip_choice=(('o','oneway'),('r','roundtrip'),)
    trip=models.CharField(max_length=5, choices=trip_choice)
    price= models.DecimalField(max_digits=10,decimal_places=2,null=True) #example: 25648910,50
    seat = models.CharField(max_length=255,null=True)
    registereduser =models.ForeignKey(RegisteredUser,null=True,on_delete= models.SET_NULL)
    ticketclass = models.ForeignKey(Ticketclass, on_delete=models.CASCADE, null=True)  # Inheritence
    flight = models.ManyToManyField(Flight)

