from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.conf import settings

#İrfan Ege Saray

# Create your models here.

#Problem çıkmasını engellemek için geliştirme sürecinde hepsi null=True , son sürümde güncellenecektir.


#********************************ÖNEMLİ*******************************
# şifrelerin gizlenmesi,authentication gibi özellikler için djangonun sağladığı userı kullanıyoruz
# ancak user ın başka şeylerle bağlantı kurması gerekiyor örneğin uçak bileti, bundan dolayı RegisteredUser tablosu oluşturuyoruz
# ve bu tablo django'nun userı ile OneToOne relation kuruyor. Bir kişi kayıt olduğunda o kişi için registeredUser tablosu oluşması gerek
# ve bunun nasıl yapılacağına dair internette kaynaklar mevcut
#********************************ÖNEMLİ*******************************

class RegisteredUser(models.Model):

    user= models.OneToOneField(User,null=True,on_delete=models.CASCADE)   ## realation with django's user

    first_name = models.CharField(max_length=255,null=True)
    last_name = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=11, null=True)
    email = models.EmailField(max_length=254)
    date_created = models.DateField(auto_now_add=True,null=True)

    def __str__(self):
        return self.last_name


class CreditCard(models.Model):
    cardNumber= models.DecimalField(max_digits=16,decimal_places=0 , primary_key=True)
    cardName= models.CharField(max_length=255,null=True)
    expirationDate=models.DateField(auto_now_add=False,auto_now=False,null=True)# form ile uyumsuzluk olursa integer yapılabilir
    cvv = models.DecimalField(max_digits=3,decimal_places=0,null=True)
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
    feedback_id = models.CharField(max_length=255,primary_key=True)
    type= models.CharField(max_length=255,null=True,choices=TYPE)
    text= models.CharField(max_length=1000,null=True)
    registereduser =models.ForeignKey(RegisteredUser,null=True,on_delete= models.SET_NULL)

    def __str__(self):
        return self.feedback_id


class Airport(models.Model):
    id= models.CharField(max_length=10 ,primary_key=True)
    name=models.CharField(max_length=255,null=True)
    address=models.CharField(max_length=500,null=True)
    def __str__(self):
        return self.name


class Flight(models.Model):
    pnr=models.CharField(max_length=10,primary_key=True)
    fligthdate=models.DateField(auto_now_add=False,auto_now=False,null=True)
    destinations = models.ManyToManyField(Airport)  # ilk seçilen kalkış, aradakiler aktarma,son seçilen varış olabilir??!!
    def __str__(self):
        return self.pnr


class ChildTicket(models.Model):
    privilages=models.CharField(max_length=500,null=True)
    name=models.CharField(max_length=500,null=True)
    extraprice=models.DecimalField(max_digits=10,decimal_places=2,null=True)
    def __str__(self):
        return self.name

class Ticket(models.Model):
    id= models.CharField(max_length=10 ,primary_key=True)
    price= models.DecimalField(max_digits=10,decimal_places=2,null=True) #example: 25648910,50
    seat = models.CharField(max_length=255,null=True)
    tickettype =models.ForeignKey(ChildTicket,on_delete=models.CASCADE,null=True)        #Inheritence
    flights = models.ManyToManyField(Flight)
    registereduser =models.ForeignKey(RegisteredUser,null=True,on_delete= models.SET_NULL)
    def __str__(self):
        return self.id

