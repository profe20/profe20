from django import forms
from .models import propertyBook
from ckeditor.widgets import CKEditorWidget
from ckeditor.widgets import CKEditorWidget

class PostForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model= Post
        fields = ['title' , 'content' , 'image' ,]




