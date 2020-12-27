from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#********************************************Eski deneme DB*************************************************
# class user(models.Model):
#     name = models.CharField(max_length=200, null=True)
#     phone = models.CharField(max_length=200, null=True)
#     email = models.CharField(max_length=200, null=True)
#     date_created = models.DateTimeField(auto_now_add=True, null= True)
#
#     def __str__(self):
#         return self.name
#
# class ticket(models.Model):
#     time = models.CharField(max_length=200, null=True)
#     seat = models.CharField(max_length=200, null=True)
#     nofpassengers = models.FloatField(null=True)
#     departure = models.CharField(max_length=200, null=True)
#     destination = models.CharField(max_length=200, null=True)
#     price = models.FloatField(null=True)
#     date_created = models.DateTimeField(auto_now_add=True, null=True)
#
# class Order(models.Model):
#     user = models.ForeignKey(user, null=True, on_delete= models.SET_NULL)
#     ticket = models.ForeignKey(ticket, null=True, on_delete= models.SET_NULL)
#     date_created = models.DateTimeField(auto_now_add=True, null=True)
#     status = models.CharField(max_length=200, null=True)
#
#
# class Comment(models.Model):
#     product = models.ForeignKey(ticket, on_delete=models.CASCADE, related_name='comments')
#     comment_content = models.TextField()
#     commenter = models.ForeignKey(User, on_delete=models.CASCADE)
#     created_on = models.DateTimeField(auto_now_add=True)
#     active = models.BooleanField(default=False)
#
#     class Meta:
#         ordering = ['-created_on']
#
#     def __str__(self):
#         return f'{self.comment_content} by {self.commenter}'
#********************************************Eski deneme DB*************************************************



#REGISTEREDUSER bize django tarafından sağlanacak
#içeriği : first_name
#        : last_name
#        : username *** V1.0 Rad class diagram da yok sonradan eklenebilir
#        : email
#        : password
#        : phoonenumber  *** djangonun sağladığı user içinde yok nasıl ekleneceği çözülecek!!!!!
#*******************************************************
#ADMIN bize django tarafından sağlanacak
#içeriği : username
#        : password
#*******************************************************




#Problem çıkmasını engellemek için geliştirme sürecinde hepsi null=True , son sürümde güncellenecektir.
class CreditCard(models.Model):
    cardNumber= models.DecimalField(max_digits=16,decimal_places=0 , primary_key=True)
    cardName= models.CharField(max_length=255,null=True)
    expirationDate=models.DateField(auto_now_add=False,auto_now=False,null=True)# form ile uyumsuzluk olursa integer yapılabilir
    cvv = models.DecimalField(max_digits=3,decimal_places=0,null=True)
    cardHolderName = models.CharField(max_length=255,null=True)
    #RegisteredUseremail  foreign key ????!!!!?
    def __str__(self):
        return self.cardName


class Feedback(models.Model):
    TYPE = (
        ('request','request'),
        ('suggestion','suggestion'),
        ('complaint','complaint')
    )
    feedback_id = models.DecimalField(max_digits=10,decimal_places=0,primary_key=True)
    type= models.CharField(max_length=255,null=True,choices=TYPE)
    text= models.CharField(max_length=1000,null=True)
    # RegisteredUseremail  foreign key ????!!!!?

    def __str__(self):
        return self.feedback_id




#Ticket inheritence doğru değil!?!?!?!


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
    tag =models.ManyToManyField(ChildTicket)
    # RegisteredUseremail  foreign key ????!!!!?
    def __str__(self):
        return self.id

# ***************eski********************
# class EconomyTicket(models.Model):
#     economy_priviliges = models.CharField(max_length=500,null=True)
#     Ticketid=models.ForeignKey(Ticket,null=True,on_delete=models.CASCADE)#on_delete???
#
# class BusinessTicket(models.Model):
#     business_priviliges = models.CharField(max_length=500,null=True)
#     Ticketid=models.ForeignKey(Ticket,null=True,on_delete=models.CASCADE)#on_delete???
#
# class FirstClassTicket(models.Model):
#     firstclass_priviliges = models.CharField(max_length=500,null=True)
#     Ticketid=models.ForeignKey(Ticket,null=True,on_delete=models.CASCADE)#on_delete???
# ***************eski********************

class Flight(models.Model):
    pnr=models.DecimalField(max_digits=10,decimal_places=0,null=True)
    fligthdate=models.DateField(auto_now_add=False,auto_now=False,null=True)


class Airport(models.Model):
    id= models.CharField(max_length=10 ,primary_key=True)
    name=models.CharField(max_length=255,null=True)
    address=models.CharField(max_length=500,null=True)


class Ticket_Flight(models.Model):
    Ticketid =models.ForeignKey(Ticket,null=True,on_delete=models.SET_NULL)
    Flightpnr =models.ForeignKey(Flight,null=True,on_delete=models.SET_NULL)


class Airport_Flight(models.Model):
    departure_arrival =models.ManyToManyField(Airport) #ilk seçilen kalkış, aradakiler aktarma,son seçilen varış olabilir??!!
    Flightpnr = models.ForeignKey(Flight, null=True, on_delete=models.SET_NULL)


