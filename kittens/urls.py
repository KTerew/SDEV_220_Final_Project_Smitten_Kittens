from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page 
    path("kitten/<int:pk>/", views. kitten_detail,  # Detail page for individual kitten
          name="kitten_detail"),  # <int:pk> captures the kitten's primary key from the URL
]