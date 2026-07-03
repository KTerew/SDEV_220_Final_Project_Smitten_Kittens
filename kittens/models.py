from django.db import models
from django.utils import timezone
from django.conf import settings

class Listing(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, 
                              on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Listing #{self.id} - {self.owner.username}"

class Kitten(models.Model):
    listing = models.ForeignKey(Listing,on_delete=models.CASCADE,
                                related_name='kittens')  # Allows accessing all kittens from a listing using listing.kittens.all()
    name = models.CharField(max_length=20)
    description = models.TextField()
    available = models.BooleanField(default=True)
    photo = models.ImageField(upload_to="kittens/",default='default/Kitten_Default.png')
            # photos uploaded are added to the media/kittens folder
            # if no photo is uploaded, a default photo is added

    def __str__(self):
        return self.name
