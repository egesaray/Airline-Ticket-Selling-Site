from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from home.models import *
from django.forms import ModelForm


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
   #
   # def __init__(self, **kwargs):
   #    self.registereduser = kwargs.pop('registereduser', None)
   #    super(AddCreditCardForm, self).__init__(**kwargs)
   #
   # def save(self, commit=True):
   #    obj = super(AddCreditCardForm, self).save(commit=False)
   #    obj.registereduser = self.registereduser
   #    if commit:
   #       obj.save()
   #    return obj
   #

   class Meta:
      model = CreditCard
      fields = ['cardName', 'cardNumber', 'expiration', 'cvv', 'cardHolderName', 'registereduser']
      widgets = {
         'cardName': forms.TextInput(attrs={'class': 'form-control'}),
         'cardNumber': forms.TextInput(attrs={'class': 'form-control'}),
         'expiration': forms.TextInput(attrs={'class': 'form-control'}),
         'cvv': forms.TextInput(attrs={'class': 'form-control'}),
         'cardHolderName': forms.TextInput(attrs={'class': 'form-control'}),
      }
