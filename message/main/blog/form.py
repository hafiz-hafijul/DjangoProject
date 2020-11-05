from django import forms
from .models import User


class StudentData(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'password']
        widgets = {'password': forms.PasswordInput}