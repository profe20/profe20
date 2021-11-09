from django.db import models

# Create your models here.
class about (models.Model):
    
     Who We Are=models.TextField(max_length=1000)
    Robertho Garcia= models.CharField(max_length=50)
    Our Story=models.TextField(max_length=1000)
    Our Values =models.TextField(max_length=1000)

    title3 = models.CharField(max_length=50)
    image = models.ImageField(upload_to="main_product"  ,blank=True, null=True)