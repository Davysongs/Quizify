from django import forms
from .models import User


class SignForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username", "password", "email", "gender")
        widgets = {
            "username" : forms.TextInput(attrs = {"class":"custom", "placeholder":"ex: John Doe"}),
            "password" : forms.PasswordInput(attrs = {"class":"custom",  "placeholder":"Create a strong password"}),
            "email": forms.EmailInput(attrs = {"class":"custom", "placeholder":"ex: sample@gmail.com"}),
            "gender": forms.Select(attrs = {"class":"custom"}),
        }
    #form validation -- check if user already exists
        
    def save(self, commit=True):
        #PASSWORD HASHING
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

class LogForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("email", "password")
        widgets = {
            "password" : forms.PasswordInput(attrs = {"class":"input"}),
             "email": forms.EmailInput(attrs = {"class":"input"})
        }
