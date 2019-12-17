from django import forms
from django.forms import modelformset_factory
from .models import studtovedom

class LogForm(forms.Form):
    login = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'size':30 , 'class':'form-control'}))
    password = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'type' : 'password', 'class' : 'form-control',  'id' : 'inputPassword'}))
    
    
class StudForm(forms.Form):

    def form():
        return modelformset_factory(studtovedom, fields=('id_vedom' ,'id_stud' ,'value'), 
        #labels = {'name' : ''}, 
        widgets={'id_vedom': forms.TextInput(attrs={'readonly': True, 'class' : 'form-control'}), 
        'id_stud' : forms.TextInput(attrs={'readonly': True, 'class' : 'form-control'})}, 
        extra=0)