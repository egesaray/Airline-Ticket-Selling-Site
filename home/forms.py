from django import forms
from .models import Comment
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from home.models import user




class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment_content',)


class ContactForm(forms.Form):
    username = forms.CharField(required=True)
    from_email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
