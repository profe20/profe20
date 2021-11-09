from django import forms
from .models import cairotourBook


class DateInput(forms.DateInput):
      input_type = 'date'

class cairotourBookForm(forms.ModelForm):

    class Meta:
        model= cairotourBook
        fields = ['phone_number' , 'guest' , 'datesfrom' ]


        widgets = {
        
            'datesfrom': DateInput(),
         }
