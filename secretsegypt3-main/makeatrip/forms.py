from django import forms
from .models import makeatrip


class DateInput(forms.DateInput):
      input_type = 'date'

class makeatripForm(forms.ModelForm):

    class Meta:
        model= makeatrip
        fields = ['luxor' , 'aswan' , 'cairo','giza' , 'hurghada' , 'Departure', 'arrival','guest','name' , 'nationality' , 'phone_number', ]

        widgets = {
            'Departure': DateInput(),
            'arrival': DateInput(),

         }
