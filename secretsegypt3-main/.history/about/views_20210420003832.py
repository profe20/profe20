from django.shortcuts import render
from django.shortcuts import render, get_object_or_404 ,redirect
from django.views.generic.edit import FormMixin

from django.views.generic import  ListView 

from .models import about
from.forms import  aboutList
# Create your views here.


class aboutList(ListView):   
    model=aboutList
    ##filer
  
  
