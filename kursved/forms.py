from django import forms
from django.forms import modelformset_factory
from .models import stud

class LogForm(forms.Form):
    login = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'size':30 , 'class':'form-control'}))
    password = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'type' : 'password', 'class' : 'form-control',  'id' : 'inputPassword'}))
    
    
class StudForm(forms.Form):

    def form():
        return modelformset_factory(stud, fields=('surname','name'), extra=0)