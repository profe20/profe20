from django import forms
from .models import propertyBook



class propertyBookForm(forms.ModelForm):
   
    class Meta:
        model= propertyBook
        fields = ['propertyBook' , 'guest' , 'guest' ,]




