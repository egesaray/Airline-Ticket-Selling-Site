from django.urls import path
from . import views
from airline import settings
from django.conf.urls.static import static
urlpatterns = [
    # leave as empty string fo base url
    path('', views.home),
    path('login/', views.login),
    path('register/', views.register),
    path('homepage/', views.homepage),



   ]
