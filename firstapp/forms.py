from django import forms
from .models import *
class  UserForm(forms.Form):
    name = forms.CharField(label='Тема', max_length=100)
    text =forms.CharField(label='Текст',
    widget=forms.Textarea(attrs={'rows': 10,'style': 'width:360px'}))
    image  = forms.ImageField(label='Файл')
    required_css_class = "field"
