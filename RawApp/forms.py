from django import forms
from .models import User, Questions


class SignForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
class LogForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "email", "password"
        widgets = {
            "password" : forms.PasswordInput()
        }