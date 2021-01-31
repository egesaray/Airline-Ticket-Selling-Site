
import django_filters
from django import forms
from .models import *


class FlightFilter(django_filters.FilterSet):
    class Meta:
        model=Flight
        fields = ['departure_time','from_airport','to_airport']
