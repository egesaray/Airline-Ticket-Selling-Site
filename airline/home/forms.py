from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.forms import ModelForm
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
   first_name = forms.CharField()
   last_name = forms.CharField()
   phone = forms.CharField()
   email = forms.CharField()

   class Meta:
      model = User
      fields = ['username', 'first_name', 'last_name', 'phone', 'email', 'password1', 'password2']

class ContactForm(ModelForm):
   class Meta:
      model = Feedback
      fields = ['text', 'type']
      widgets = {
          'text': forms.Textarea(attrs={'class': 'form-control'}),
      }

class ResponseForm(ModelForm):
   class Meta:
      model = Feedback
      fields = ['adminresponse' ]
      widgets = {
          'adminresponse': forms.Textarea(attrs={'class': 'form-control'}),
      }

class ChangeEmailForm(ModelForm):
   class Meta:
      model=RegisteredUser
      fields = ['first_name','last_name','email','phone']
      widgets = {     # django formları için css style
         'first_name': forms.TextInput(attrs={'class': 'form-control'}),
         'last_name': forms.TextInput(attrs={'class': 'form-control'}),
         'phone': forms.TextInput(attrs={'class': 'form-control'}),
         'email': forms.TextInput(attrs={'class': 'form-control'}),
      }

class AddCreditCardForm(ModelForm):
   class Meta:
      model=CreditCard
      fields =['cardName','cardNumber','expirationmonth','expirationyear' ,'cvv' ,'cardHolderName']
      widgets = {
         'cardName': forms.TextInput(attrs={'class': 'form-control'}),
         'cardNumber': forms.TextInput(attrs={'class': 'form-control'}),
         'cvv': forms.TextInput(attrs={'class': 'form-control'}),
         'cardHolderName': forms.TextInput(attrs={'class': 'form-control'}),
      }

class addflight(forms.ModelForm):
   class Meta:
      model = Flight
      fields = ['pnr', 'departure_time', 'arrival_time', 'departure_hour', 'arrival_hour', 'from_airport', 'to_airport', 'price']


class addAirport(forms.ModelForm):
   class Meta:
      model = Airport
      fields = ['name', 'address']


class chooseflight(forms.ModelForm):
   class Meta:
      model = Flight
      fields = ['from_airport', 'to_airport']
      exclude = ['pnr', 'departure_time', 'arrival_time', 'departure_hour', 'arrival_hour', 'price']



class SeatSelection(forms.ModelForm):
      class Meta:
         model = Aseat
         fields = ['seat' , 'passangerName' , 'passangerTC']





