from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from .models import *
from django.utils.translation import ugettext_lazy as _

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

    def creditcards(self):
        return self.save()


class Feedback(models.Model):
    TYPE = (
        ('request','request'),
        ('suggestion','suggestion'),
        ('complaint','complaint')
    )

    type= models.CharField(max_length=255,null=True,choices=TYPE)
    text= models.TextField()
    registereduser =models.ForeignKey(RegisteredUser,null=True,on_delete= models.SET_NULL)




class Airport(models.Model):
    name=models.CharField(max_length=255,null=True)
    address=models.CharField(max_length=500,null=True)

    def __str__(self):
        return self.name


class Flight(models.Model):
    pnr=models.CharField(max_length=10, null=True)
    departure_time = models.DateField(auto_now_add=False, auto_now=False, null=True)
    arrival_time = models.DateField(auto_now_add=False, auto_now=False, null=True)
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
    registereduser =models.ForeignKey(RegisteredUser,null=True,on_delete= models.SET_NULL)
    ticket_class = models.CharField(max_length=255,null=True)
    flight = models.ForeignKey(Flight,null=True,on_delete=models.CASCADE)
    ticket_price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    created_at = models.CharField(max_length=255,null=True)
    is_approval = models.CharField(max_length=1, null=True)


    def __str__(self):
        return self.ticket_class

    def chooseclass(self):
        return self.save()