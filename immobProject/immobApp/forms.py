from django import forms

from .models import Inscription


class IntegrationForm(forms.ModelForm):
    class Meta : 
        model = Inscription
        fields = ['nom','prenom','email','numero_tel','ville']

    