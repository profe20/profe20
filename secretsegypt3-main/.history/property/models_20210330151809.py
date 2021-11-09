from django.db import models
from django.utils.translation import gettext as _
from django.utils import timezone

# Create your models here.
class property(models.Model):
    
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="main_product"  ,blank=True, null=True)
    price=models.IntegerField(default=0)
    description=models.TextField(max_length=1000)
    property = models.ForeignKey(property, on_delete=models.CASCADE)

    created = models.DateTimeField(default=timezone.now)
    active  = models.BooleanField(default=True)
    
    
class properImages(models.Model):
       property = models.ForeignKey(property, on_delete=models.CASCADE)
       image = models.ImageField(upload_to="main_product"  ,blank=True, null=True)
 
 class place(models.Model):
     
      name = models.CharField(max_length=50)
      image = models.ImageField(upload_to="main_product"  ,blank=True, null=True)
 
 class category(models.Model):
     
     category = models.CharField(max_length=40)
 
 