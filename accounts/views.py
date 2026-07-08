from django.shortcuts import render, redirect 
from django.contrib.auth.forms import UserCreationForm

def register(request):
    form = UserCreationForm()  #Create an empty registration form

    # Render the register page and pass the form into template
    return render(request, "accounts/register.html",{
        "form" : form}
    )


