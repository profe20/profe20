from django import forms
from .models import luxortourBook


class DateInput(forms.DateInput):
      input_type = 'date'

class luxortourBookForm(forms.ModelForm):

    class Meta:
        model= luxortourBook
        fields = ['phone_number' , 'guest' , 'datesfrom' ]

        widgets = {
            'datesfrom': DateInput(),
         }
