from django import forms
from .models import propertyBook
from ckeditor.widgets import CKEditorWidget
from ckeditor.widgets import CKEditorWidget

class propertyBookForm(forms.ModelForm):
    
    class Meta:
        model= propertyBook
        fields = ['title' , 'content' , 'image' ,]




