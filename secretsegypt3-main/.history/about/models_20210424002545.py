from django.db import models

# Create your models here.
class about (models.Model):
    
  Who_We_Are=models.TextField(max_length=1000)     
  Who_image = models.ImageField(upload_to="main_product"  ,blank=True, null=True)
  Our_Story=models.TextField(max_length=1000)
  Our_image = models.ImageField(upload_to="main_product"  ,blank=True, null=True)
  Our_Values2 =models.TextField(max_length=1000)
  Our_Values = models.ImageField(upload_to="main_product"  ,blank=True, null=True)
  
  
  def __str__(self):
       return self.Who_We_Are