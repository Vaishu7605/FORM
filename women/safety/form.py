from django import forms
from .models import *

class clientform(forms.ModelForm):
    class Meta:
        model=register
        fields='__all__'
        widgets={
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'password':forms.TextInput(attrs={'class':'form-control'}),
            'confirm_password':forms.TextInput(attrs={'class':'form-control'}),
            'contact_number':forms.TextInput(attrs={'class':'form-control'})

        }