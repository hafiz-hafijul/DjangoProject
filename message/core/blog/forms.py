from django import forms
from .models import User

class ShowData(forms.ModelForm):
    class Meta:
        model=User
        fields = ['name', 'email', 'password']
        widgets = {'password':forms.PasswordInput}