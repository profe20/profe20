from django import forms
from .models import Post
from ckeditor.widgets import CKEditorWidget
from ckeditor.widgets import CKEditorWidget
from .models import student
from .models import request

class PostForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model= Post
        fields = ['title' , 'content' , 'image' ,]


class studentForm(forms.ModelForm):
    class Meta:
        model= student
        fields = ['nemee' , 'univer1' , 'college1' ,'study1','band1','Section1','phone1','email1','image1','image3']




