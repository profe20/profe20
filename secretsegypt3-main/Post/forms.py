from django import forms
from .models import Post,Comment
from ckeditor.widgets import CKEditorWidget
from ckeditor.widgets import CKEditorWidget

class PostForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model= Post
        fields = ['title' , 'content' , 'image' ,'image1' , 'image2']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body','image')
