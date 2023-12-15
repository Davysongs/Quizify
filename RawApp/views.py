from django.shortcuts import render
from .models import User
import requests
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from RawApp.forms import SignForm


# Create your views here.
#signup
@csrf_exempt
def register(request):
    user_info = SignForm()
    if request.method == "POST":
        u_name = request.POST.get("u_name")
        u_email = request.POST.get("u_email")
        u_password = request.POST.get("u_password")

        if not u_name or not u_email or not u_password:
            return render(request, "sign-up.html", {'error': 'Please fill in all fields.'} )
        
        user_info = SignForm(request.POST)
        if user_info.isvalid():
            user_info.save()
        return render(request, "login.html")
    context = {"form": user_info}
    return render(request, "sign-up.html", context)

#login 
def login (request):
    if request.method == "POST":
        u_email = request.POST.get("u_email")
        u_password = request.POST.get("u_password")
        if not u_email or not u_password:
            return render(request, "login.html", {'error': 'Please fill in all fields.'} )
        user_info = User.objects.filter(email = u_email)
        if user_info:
            if user_info[0].password == u_password:
                return render(request, "home.html")
            else:
                return render(request, "login.html", {'error': 'Invalid password.'})
        else:
            return render(request, "login.html", {'error': 'User not found.'})
    return render(request, "login.html")    
def main(request):
    return render(request, "index.html")