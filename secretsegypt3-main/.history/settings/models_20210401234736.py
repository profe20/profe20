from django.db import models

# Create your models here.


class settings (models.Model):

  site_name=models.CharField(max_length=50)
  logo  = models.ImageField(upload_to='settings/')
  phone=models.CharField(max_length=20)
  email = models.EmailField(max_length = 254)
  description=models.TextField(max_length=1000)


  