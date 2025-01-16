from django.forms import ModelForm
from .models import *
from django import forms

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['desc']
    
    
        