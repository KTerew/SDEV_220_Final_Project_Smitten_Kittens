from django.shortcuts import render, get_object_or_404, redirect
from .models import Listing, Kitten
from .forms import KittenForm, ListingForm
from .utils import zipcode_to_city
# TEMP
from django.contrib.auth import get_user_model




def home(request):
    listings = Listing.objects.filter(kittens__isnull=False).distinct()  # Homepage only shows listings with kittens in them

    if request.method == "POST":
        form = ListingForm(request.POST)
        if form.is_valid():
            listing = form.save(commit=False)

            # TEMP FIX (since login is not merged yet)
            User = get_user_model()
            listing.owner = User.objects.first()

            listing.save()
            return redirect("create_kitten", listing_id=listing.pk)
    else:
        form = ListingForm()

    return render(request, "kittens/home.html", {
        "listings": listings, # Pass listings from view to template for display
        "form":form}
    )

def kitten_detail(request, kitten_id):
    kitten = get_object_or_404(Kitten, pk=kitten_id)  # Retrieve kitten with PrimaryKey only if it exists

        # Convert kitten's zipcode into city and state using pgeocode
    city, state = zipcode_to_city(kitten.zipcode)

        # Pass data to template
    return render(request, "kittens/kitten_detail.html", {
        "kitten": kitten,
        "city": city,
        "state": state}  
    )


def create_kitten(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    kittens = listing.kittens.all()

    if request.method == "POST":
        form = KittenForm(request.POST, request.FILES)
        if form.is_valid():
            kitten = form.save(commit=False)
            kitten.listing = listing
            kitten.save()
            return redirect("create_kitten", listing_id=listing.pk)
    else:
        form = KittenForm()

    return render(request, 'kittens/kitten_edit.html',
                   {'form':form,
                    'listing':listing,
                    "kittens": kittens,}
                    )

def edit_kitten(request, kitten_id):
    kitten = get_object_or_404(Kitten, pk=kitten_id)

    if request.method == "POST":
        form = KittenForm(request.POST, request.FILES, instance=kitten)

        if form.is_valid():
            form.save()
            return redirect("create_kitten", listing_id=kitten.listing.pk)

    else:
        form = KittenForm(instance=kitten)

    return render(
        request,
        "kittens/kitten_edit.html",
        {
            "form": form,
            "kitten": kitten,
            "listing": kitten.listing,
            "kittens": kitten.listing.kittens.all(),
        },
    )


def delete_kitten(request, kitten_id):
    kitten = get_object_or_404(Kitten, pk=kitten_id)

    if request.method == "POST":
        listing_id = kitten.listing.id
        kitten.delete()

        return redirect("create_kitten", listing_id=listing_id)

    return render(
        request,
        "kittens/delete_kitten.html",
        {"kitten": kitten}
    )