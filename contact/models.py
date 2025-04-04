from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# criar depois
#category(foreign key), show(boolean), owner(foreign key)
#picture(image)


# Create your models here.



class Category(models.Model):

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=50)
    def __str__(self):
        return f'{self.name}'

class Contact(models.Model):

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=12)
    email = models.EmailField(max_length=254)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    show = models.BooleanField(default=True)
    picture = models.ImageField(blank=True, upload_to='pictures/%Y/%m')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'