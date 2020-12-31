from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from home.models import RegisteredUser


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

