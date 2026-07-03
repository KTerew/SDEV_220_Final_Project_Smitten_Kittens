from django.shortcuts import render
from .models import Listing


def home(request):
    listings = Listing.objects.filter(kittens__isnull=False).distinct()  # Homepage only shows listings with kittens in them
    return render(request, "kittens/home.html", {
        "listings": listings}  # Pass listings from view to template for display
    )