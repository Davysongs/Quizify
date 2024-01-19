from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username","email","password1", "password2"]
        #     "username" : forms.TextInput(attrs = {"class":"custom", "placeholder":"ex: John Doe"}),
        #     "password1" : forms.PasswordInput(attrs = {"class":"custom",  "placeholder":"Create a strong password"}),
        #     "email": forms.EmailInput(attrs = {"class":"custom", "placeholder":"ex: sample@gmail.com"}),
        # }


# class LogForm(AuthenticationForm):
#     class Meta:
#         model = User
#         fields = ["username", "password"]
#         widgets = {
#             "password" : forms.PasswordInput(attrs = {"class":"input"}),
#              "username": forms.TextInput(attrs = {"class":"input"})
#         }
        
