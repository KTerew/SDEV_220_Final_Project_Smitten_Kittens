from django.shortcuts import render, get_object_or_404
from .models import Listing, Kitten


def home(request):
    listings = Listing.objects.filter(kittens__isnull=False).distinct()  # Homepage only shows listings with kittens in them
    return render(request, "kittens/home.html", {
        "listings": listings}  # Pass listings from view to template for display
    )

def kitten_detail(request, pk):
    kitten = get_object_or_404(Kitten, pk=pk)  # Retrieve kitten with PrimaryKey only if it exists
    return render(request, "kittens/kitten_detail.html", {
        "kitten": kitten}  # Render detail page and pass selected kitten to template
    )