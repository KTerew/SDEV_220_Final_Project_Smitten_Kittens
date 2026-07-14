from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page 
    path("kitten/<int:kitten_id>/", views. kitten_detail,  # Detail page for individual kitten
          name="kitten_detail"),  # <int:pk> captures the kitten's primary key from the URL
    path("listing/<int:listing_id>/kittens/new/",
          views.create_kitten, name="create_kitten"),
      path("kitten/<int:kitten_id>/edit/", views.edit_kitten, name="edit_kitten",),
      path("kitten/<int:kitten_id>/delete/",views.delete_kitten,name="delete_kitten"),
]