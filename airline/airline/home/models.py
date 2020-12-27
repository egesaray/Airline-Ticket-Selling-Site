from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class user(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null= True)

    def __str__(self):
        return self.name

class ticket(models.Model):
    time = models.CharField(max_length=200, null=True)
    seat = models.CharField(max_length=200, null=True)
    nofpassengers = models.FloatField(null=True)
    departure = models.CharField(max_length=200, null=True)
    destination = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

class Order(models.Model):
    user = models.ForeignKey(user, null=True, on_delete= models.SET_NULL)
    ticket = models.ForeignKey(ticket, null=True, on_delete= models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True)


class Comment(models.Model):
    product = models.ForeignKey(ticket, on_delete=models.CASCADE, related_name='comments')
    comment_content = models.TextField()
    commenter = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f'{self.comment_content} by {self.commenter}'