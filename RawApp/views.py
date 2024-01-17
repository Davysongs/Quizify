from django.shortcuts import render, redirect
from .models import User
import requests
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from RawApp.forms import SignForm, LogForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
#Home page 
def main(request):
    return render(request, "index.html")

#signup
def register(request):
    form = SignForm()
    if request.method == 'POST':
        form = SignForm(request.POST)
        if form.is_valid():
            #check if user alredy exists before saving

            user = form.save()
            return Response ("Hi its done")
            #render htmx that says sign up successful into the login form

        context = {"form" : form}
        return render (request, "login.html")
        
    elif request.method == "GET":
        context = {"form" : form}
        return render(request, "sign-up.html", context)



#login 
def login (request):
    form = LogForm()
    if request.method == "POST":
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect("base.html")
            #check if user already exists and give an error message if user doesn't


            #give an error message if user password is incorrect

            # the login session should direct authenticated user to the QuizMgt App { the return is temporary for testing purpose}

            
    context = {"form": form}
    return render(request, "login.html", context)  

#Main user dashboard page
@login_required
def dashboard(request):
    return render(request, "home.html", {"section":"dashboard"})

