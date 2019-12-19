from django import forms
from django.forms import modelformset_factory
from .models import studtovedom

class LogForm(forms.Form):
    login = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'size':30 , 'class':'form-control'}))
    password = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'size':30, 'type' : 'password', 'class' : 'form-control',  'id' : 'inputPassword'}))
    
StudForm = modelformset_factory(studtovedom, fields=('value',),
       labels = {'value' : ''},
       #widgets = {'value' : forms.Select({'disabled' : True})},
       extra=0)