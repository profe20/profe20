from django.shortcuts import render

from django.views.generic import  ,ListView ,DetailView

from .models import property

# Create your views here.


class PropertyList(ListView):   
    model=property
    ##filer
  
  
class propertyDetail(DetailView):
    pass
    ##books  