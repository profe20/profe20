from django import forms
from .models import cnilecruiseBook


class DateInput(forms.DateInput):
      input_type = 'date'

class nilecruiseBookForm(forms.ModelForm):

    class Meta:
        model= cnilecruiseBook
        fields = ['phone_number' , 'guest' , 'datesfrom' ]

        widgets = {
            'datesfrom': DateInput(),
         }
