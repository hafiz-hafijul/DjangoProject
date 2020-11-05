from django import forms
from .models import User

class Registration(forms.ModelForm):
    class Meta:
        model = User

        fields = ['name', 'email', 'password']