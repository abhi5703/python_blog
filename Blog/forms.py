from django import forms
from django.forms import ModelForm
from .models import Blog

class BlogForm(forms.ModelForm):
    class Meta:
        model= Blog
        fields= "__all__"
        widgets ={
            'BlogId'     :forms.TextInput(attrs={'class':'form-control'}),
            'Title'      :forms.TextInput(attrs={'class':'form-control'}),
            'Author_Name':forms.TextInput(attrs={'class':'form-control'}),
            'Start_Date' :forms.TextInput(attrs={'class':'form-control'}),
            'End_Date'   :forms.TextInput(attrs={'class':'form-control'}),
        }