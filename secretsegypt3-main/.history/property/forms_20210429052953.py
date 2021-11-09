from django import forms
from .models import propertyBook



class propertyBookForm(forms.ModelForm):
   
    class Meta:
        model= propertyBook
        fields = ['phone_number' , 'guest' , 'datesfrom' ]

       widgets = {
            'datesfrom': DateInput(),
         }
