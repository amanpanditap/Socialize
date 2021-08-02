from django import forms
from django.forms import fields
from .models import Post, Comment

class PostModelForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}))
    class Meta:
        model = Post
        fields = ('content','image')

class CommentModelForm(forms.ModelForm):
    body = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Add a Comment...'}))
    class Meta:
        model = Comment
        fields = ('body',)