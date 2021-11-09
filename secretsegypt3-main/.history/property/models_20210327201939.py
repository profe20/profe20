from django.db import models
from django.utils.translation import gettext as _
from django.utils import timezone

# Create your models here.
class property(models.Model):
    
    neme=models.CharField(_("الاسم الكامل :"),max_length=100)
    Section=models.CharField(_("القسم :"),max_length=100)
    phone=models.CharField(_("تليفون  :"),max_length=12)
    email=models.EmailField(_("البريد الالكترونى الجامعى :"),max_length=254)
    image = models.FileField(_("الصورة الشخصية  :"),upload_to='profile/')
    image2 = models.FileField(_("صورة البطاقة الشخصية  :"),upload_to='profile/')
    created = models.DateTimeField(default=timezone.now)
    active  = models.BooleanField(default=True)

