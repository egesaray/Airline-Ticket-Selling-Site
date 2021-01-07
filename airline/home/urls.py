from django.urls import path
from .import views
from airline import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views

urlpatterns = [
    # leave as empty string fo base url
    path('', views.home, name="home"),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name="login"),
    path('register/', views.register, name="register"),
    path('logout/', LogoutView.as_view(next_page='home'), name="logout"),
    path('footer/', views.footer, name="footer"),
    path('header/', views.header, name="header"),


    path('homepage/', views.homepage, name="homepage"),
    path('changeEmail/', views.changeEmail, name="changeEmail"),
    path('changePassword/', views.changePassword, name="changePassword"),
    path('creditcards/', views.creditcards, name="creditcards"),
    path('delete_creditcard/<int:pk>', views.delete_creditcard, name="delete_creditcard"),


    path('completed/', views.completed, name="completed"),
    path('myflights/', views.myflights, name="myflights"),
    path('buyticket/<str:values>', views.buyticket, name="buyticket"),
    path('choose_class/<int:id>', views.choose_class, name="choose_class"),
    path('selected_flight/<int:flight_id>', views.selected_flight, name="selected_flight"),
    path('ticket_has_been_purchased/<int:id>', views.ticket_has_been_purchased, name="ticket_has_been_purchased"),

    path('ticket/', views.ticket, name="ticket"),
    path('aboutus/', views.aboutus, name="aboutus"),
    path('contactus/', views.contactus, name="contactus"),
    path('navbar/', views.navbar, name="navbar"),
    path('checkin/', views.checkin, name="checkin"),
    path('Feedback/', views.Feedback, name="Feedback"),
    path('forgotPassword/', views.forgotPassword, name="forgotPassword"),


   ]
