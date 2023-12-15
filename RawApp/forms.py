from django import forms
from .models import User

class SignForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'