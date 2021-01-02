from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from home.models import RegisteredUser
from django.forms import ModelForm


class RegistrationForm(UserCreationForm):
   first_name = forms.CharField()
   last_name = forms.CharField()
   phone = forms.CharField()
   email = forms.CharField()

   class Meta:
      model = User
      fields = ['username', 'first_name', 'last_name', 'phone', 'email', 'password1', 'password2']


class ContactForm(forms.ModelForm):
   username = forms.CharField(required=True)
   from_email = forms.EmailField(required=True)
   message = forms.CharField(widget=forms.Textarea, required=True)


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

