from django.urls import path
from . import views
from airline import settings
from django.conf.urls.static import static
urlpatterns = [
    # leave as empty string fo base url
    path('', views.home, name="home"),
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register"),
    path('homepage/', views.homepage, name="homepage"),
    path('changeEmail/', views.changeEmail, name="changeEmail"),
    path('changePassword/', views.changePassword, name="changePassword"),
    path('creditcards/', views.creditcards, name="creditcards"),
    path('footer/', views.footer, name="footer"),
    path('header/', views.header, name="header"),
    path('logout/', views.logout, name="logout"),
    path('myflights/', views.myflights, name="myflights"),
    path('ticket/', views.ticket, name="ticket"),
    path('aboutus/', views.aboutus, name="aboutus"),
    path('contactus/', views.contactus, name="contactus"),
    path('navbar/', views.navbar, name="navbar"),
    path('checkin/', views.checkin, name="checkin"),
    path('Feedback/', views.Feedback, name="Feedback"),
    path('buyticket/', views.buyticket, name="buyticket"),
    path('chooseclass/', views.chooseclass, name="chooseclass"),
    path('forgotPassword/', views.forgotPassword, name="forgotPassword"),

   ]
