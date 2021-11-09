from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import FormMixin

from django.views.generic import  ListView ,DetailView

from .models import property
from.forms import propertyBookForm
# Create your views here.


class PropertyList(ListView):   
    model=property
    ##filer
  
  
class propertyDetail(FormMixin,DetailView):
     model=property
     form_class =propertyBookForm
    ##books  
    
     def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["related"] = property.objects.filter(category=self.get_object().category)[:2]
        # ^^^ bad duplication.
        return context
    
    
     def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
           myform = form.save(commit=False)
           myform.property=self.get_objects()
           myform.save()
           return redirect('/')
          
    else:
         myform = propertyBookForm()

    context = {
        'myform' : myform ,
         }
          