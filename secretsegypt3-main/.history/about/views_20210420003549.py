from django.shortcuts import render
from django.shortcuts import render, get_object_or_404 ,redirect
from django.views.generic.edit import FormMixin

from django.views.generic import  ListView 

from .models import property
from.forms import propertyBookForm
# Create your views here.


class aboutList(ListView):   
    model=aboutList
    ##filer
  
  
