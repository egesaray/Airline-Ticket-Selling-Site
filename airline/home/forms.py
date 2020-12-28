from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *

class ContactForm(forms.ModelForm):
   username = forms.CharField(required=True)
   from_email = forms.EmailField(required=True)
   message = forms.CharField(widget=forms.Textarea, required=True)

