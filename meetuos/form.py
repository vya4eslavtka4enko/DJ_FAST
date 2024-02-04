from django.apps import forms

from .models import Participant

class RegistrationForm(form.ModelForm): 
    class Meta:
        model = Participant
        fields = ['email']
        
        