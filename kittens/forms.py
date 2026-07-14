from django import forms
from .models import Kitten, Listing

class KittenForm(forms.ModelForm):
    class Meta:
        model = Kitten
        fields = (
            'name',
            'description',
            'available',
            'photo',
            'gender',
            'spayed',
            'zipcode'
            )


class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = [] 