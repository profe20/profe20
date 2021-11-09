from django import forms
from .models import aswanBook


class DateInput(forms.DateInput):
      input_type = 'date'

class aswanyBookForm(forms.ModelForm):

    class Meta:
        model= aswanBook
        fields = ['phone_number' , 'guest' , 'datesfrom' ]

        widgets = {
            'datesfrom': DateInput(),
         }
