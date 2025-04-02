from django.db import models
from django.utils import timezone

# criar depois
#category(foreign key), show(boolean), owner(foreign key)
#picture(image)


# Create your models here.

class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=12)
    email = models.EmailField(max_length=254)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'