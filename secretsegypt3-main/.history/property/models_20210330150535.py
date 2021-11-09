from django.db import models
from django.utils.translation import gettext as _
from django.utils import timezone

# Create your models here.
class property(models.Model):
    
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="main_product"  ,blank=True, null=True)
    price=models.IntegerField(default=0)
    created = models.DateTimeField(default=timezone.now)
    active  = models.BooleanField(default=True)
