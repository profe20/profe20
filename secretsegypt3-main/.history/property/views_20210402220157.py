from django.shortcuts import render

from django.views.generic import  DetailView,ListView 

from .models import property

# Create your views here.


class PropertyList(LisView):   
     model=property
    ##filer
  
  
class propertyDetail(DataiLview):
    pass
    ##books  