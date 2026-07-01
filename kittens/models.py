from django.db import models
from django.utils import timezone
from django.conf import settings

class Kitten(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, 
                              on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    description = models.TextField()
    available = models.BooleanField(default=True)
    #photo
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
