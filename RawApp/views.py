from django.shortcuts import render, redirect
from .models import User
import requests
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt

from RawApp.forms import SignForm, LogForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

# Create your views here.
#Home page 
def main(request):
    return render(request, "index.html")

#signup
class SignUp(CreateView):
    form_class = SignForm
    success_url = reverse_lazy('login')
    template_name = 'sign-up.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response


#login 
class Login(LoginView):
    template_name = "login.html"
    form_class = LogForm
    


#Logout
class Logout(LogoutView):
    next_page = reverse_lazy('main')


    
# def login (request):
#     form = LogForm()
#     if request.method == "POST":
#         if form.is_valid():
#             email = request.POST['email']
#             password = request.POST['password']
#             user = authenticate(request, email=email, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect("base.html")
            
#     context = {"form": form}
#     return render(request, "login.html", context)  

# def register(request):
#     form = SignForm()
#     if request.method == 'POST':
#         form = SignForm(request.POST)
#         if form.is_valid():
#             #check if user alredy exists before saving

#             user = form.save()
#             return Response ("Hi its done")
#             #render htmx that says sign up successful into the login form

#         context = {"form" : form}
#         return render (request, "login.html")
        
#     elif request.method == "GET":
#         context = {"form" : form}
#         return render(request, "sign-up.html", context)

