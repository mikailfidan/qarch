from django.forms import ModelForm
from .models import Post
from django import forms




class SendForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name'}), label='')
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}),label='')
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Message'}), label='')
