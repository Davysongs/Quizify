from django import forms
from .models import User, Questions


class SignForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username", "password", "email", "gender")

class LogForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "email", "password"
        widgets = {
            "password" : forms.PasswordInput()
        }