from django.db import models

# Create your models here.
class about (models.Model):
    
    title = models.CharField(max_length=50)
    title3 = models.CharField(max_length=50)
    image = models.ImageField(upload_to="main_product"  ,blank=True, null=True)