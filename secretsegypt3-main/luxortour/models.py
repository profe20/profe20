
from django.db import models
from django.utils.translation import gettext as _
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

from django.utils.text import slugify

# Create your models here.
class luxortour(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='property/')
    price=models.IntegerField(default=0)
    description=models.TextField()
    itinerary =models.TextField()
    place = models.ForeignKey('place', related_name='luxortour_place', on_delete=models.CASCADE)
    category = models.ForeignKey('category', related_name='luxortour_category', on_delete=models.CASCADE)
    created = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(null=True,blank=True) # new
    active  = models.BooleanField(default=True)


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug= slugify(self.name)
        super(luxortour,self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('luxortour:luxortour_detail', kwargs={'slug': self.slug })


class luxortourImages(models.Model):

   luxortour = models.ForeignKey('luxortour', related_name='luxortour', on_delete=models.CASCADE)
   image = models.ImageField(upload_to="main_product"  ,blank=True, null=True)

   def __str__(self):
       return str (self.luxortour)

class place(models.Model):

    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="main_product"  ,blank=True, null=True)

    def __str__(self):
        return self.name

class category(models.Model):
    category = models.CharField(max_length=40)
    def __str__(self):
        return self.category

class luxortourReview(models.Model):

 user = models.ForeignKey(User, on_delete=models.CASCADE)
 luxortour = models.ForeignKey('luxortour', related_name='Review_luxortour', on_delete=models.CASCADE)
 pricee=models.IntegerField(default=0)
 feedback=models.TextField(max_length=2000)
 created = models.DateTimeField(default=timezone.now)
 active  = models.BooleanField(default=True)

 def __str__(self):
    return str (self.luxortour)
count=(
(' 1 ', "1 "),
('2 ', "2"),
('3', "3"),
('4', "4"),
)
class luxortourBook(models.Model):
 user = models.ForeignKey(User, on_delete=models.CASCADE)
 luxortour = models.ForeignKey('luxortour', related_name='Book_luxortour', on_delete=models.CASCADE)
 phone_number = models.CharField(max_length=12)
 guest=models.CharField(choices=count ,max_length=100)
 datesfrom = models.DateTimeField(default=timezone.now)



def __str__(self):
    return str (self.luxortour)
