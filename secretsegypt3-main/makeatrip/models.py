from django.db import models

from django.utils.translation import gettext as _
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth.models import User
# Create your models here.
count=(
(' 1 ', "1 "),
('2 ', "2"),
('3', "3"),
('4', "4"),
)
class makeatrip (models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    luxor = models.ForeignKey('luxor',blank=True,null=True, related_name='luxor_category', on_delete=models.CASCADE)
    aswan = models.ForeignKey('aswan', blank=True,null=True ,related_name='aswan_category', on_delete=models.CASCADE)
    cairo = models.ForeignKey('cairo',blank=True,null=True, related_name='cairo_category', on_delete=models.CASCADE)
    giza = models.ForeignKey('giza', blank=True,null=True,related_name='giza_category', on_delete=models.CASCADE)
    hurghada = models.ForeignKey('hurghada', blank=True,null=True, related_name='hurghada_category', on_delete=models.CASCADE)
    Departure= models.DateTimeField(default=timezone.now)
    arrival = models.DateTimeField(default=timezone.now)
    guest=models.CharField(choices=count ,max_length=100)
    name = models.CharField(max_length=100)
    nationality=models.CharField(max_length=50 , blank=True, null=True)
    phone_number = models.CharField(max_length=12)
    created = models.DateTimeField(default=timezone.now)
    active  = models.BooleanField(default=True)

    def __str__(self):
       return self.name



class luxor(models.Model):
    luxor = models.CharField(max_length=40)
    def __str__(self):
        return self.luxor



class aswan(models.Model):
    aswan = models.CharField(max_length=40)
    def __str__(self):
        return self.aswan

class cairo(models.Model):
    cairo = models.CharField(max_length=40)
    def __str__(self):
        return self.cairo


class giza(models.Model):
    giza = models.CharField(max_length=40)
    def __str__(self):
        return self.giza

class hurghada(models.Model):
    hurghada = models.CharField(max_length=40)
    def __str__(self):
        return self.hurghada
