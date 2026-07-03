from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("register/", views.register, name="register"),  # Registration page  
    path("login/", auth_views.LoginView.as_view
         (template_name="accounts/login.html"),name="login"),  # Django's built-in LoginView
    path("logout/", auth_views.LogoutView.as_view(), name="logout")  # Route for logging out users - home
]