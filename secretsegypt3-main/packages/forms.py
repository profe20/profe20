from django import forms
from .models import packagesBook
from .models import Comment

class DateInput(forms.DateInput):
      input_type = 'date'

class packagesBookBookForm(forms.ModelForm):

    class Meta:
        model= packagesBook
        fields = ['phone_number' , 'guest' , 'datesfrom' ]

        widgets = {
            'datesfrom': DateInput(),
         }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'content')
