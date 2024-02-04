from django import forms

from .models import Participant

class RegistrationForm(forms.ModelForm): 
    email = forms.EmailField(label="Your email")
        
        