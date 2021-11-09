from django.db import models
from django.utils.translation import gettext as _
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class property(models.Model):
    
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="main_product"  ,blank=True, null=True)
    price=models.IntegerField(default=0)
    description=models.TextField(max_length=1000)
    place = models.ForeignKey('place', related_name='property_place', on_delete=models.CASCADE)
    category = models.ForeignKey('category', related_name='property_category', on_delete=models.CASCADE)   
    created = models.DateTimeField(default=timezone.now)
    active  = models.BooleanField(default=True) 
    
    def __str__(self):
        return self.name

class properImages(models.Model): 
  
   property = models.ForeignKey('property', related_name='proper_Images', on_delete=models.CASCADE)
   image = models.ImageField(upload_to="main_product"  ,blank=True, null=True)
   
   def __str__(self):
       return str (self.property)

class place(models.Model):
    
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="main_product"  ,blank=True, null=True)
    
    def __str__(self):
        return self.name

class category(models.Model):
    category = models.CharField(max_length=40)
    def __str__(self):
        return self.name
    
class propertyReview(models.Model):
        
 author = models.ForeignKey('User', related_name='Review_author', on_delete=models.CASCADE)
 property = models.ForeignKey('property', related_name='Review_property', on_delete=models.CASCADE)
 price=models.IntegerField(default=0)
 feedback=models.TextField(max_length=2000)
 created = models.DateTimeField(default=timezone.now)
 active  = models.BooleanField(default=True) 
    
 def __str__(self):
    return str (self.property)
count=(
(' 1 ', "1 "),
('2 ', "2"),
('3', "3"),
('4', "4"),
)
class propertyBook(models.Model):    
 user  = models.ForeignKey('User', related_name='Book_owner', on_delete=models.CASCADE)
 property = models.ForeignKey('property', related_name='Book_property', on_delete=models.CASCADE)
 phone_number = models.CharField(max_length=12) 
 guest=models.CharField(choices=count ,max_length=100)
 date_from = models.DateTimeField(default=timezone.now)
 created = models.DateTimeField(default=timezone.now)
 active  = models.BooleanField(default=True) 
 
def __str__(self):
    return str (self.property)
