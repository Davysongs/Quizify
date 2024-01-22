from django.shortcuts import render, redirect
from rest_framework.response import Response
from django.contrib import messages
from RawApp.forms import SignForm #LogForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.views.generic import ListView
from .models import Quiz
from django.utils.decorators import method_decorator
from django.http import JsonResponse


# Create your views here.
#Home page 
def main(request):
    return render(request, "index.html")

#signup
def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = SignForm()
        if request.method == 'POST':
            form = SignForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get("username")
                messages.success(request, user + "your account was created successfully")
                return redirect('login')
        elif request.method == "GET":
            context = {"form" : form}
            return render(request, "sign-up.html", context)


#login 
def signin(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request, username= username, password= password)

            if user is not None:
                login(request,user)
                return redirect("home")
            else:
                messages.info(request,"Username or password is incorrect")
        context = {}
        return render(request, "login.html", context) 



#Logout
def userlogout(request):
    logout(request)
    return redirect('login')

#homepage/dashboard
@method_decorator(login_required, name= "dispatch")
class QuizListView(ListView):
    model = Quiz
    template_name = "home.html"

@login_required(login_url= 'login')
def quiz_view(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    return render(request, "quiz.html", {'obj':quiz})

@login_required(login_url= 'login')
def quiz_data(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    questions = []
    for data in quiz.getquestions():
        answers = []
        for a in data.get_answers():
            answers.append(a.text)
        questions.append({str(data):answers})
    return JsonResponse({
        'data':questions,
       'time':quiz.time,
    })
def save_quiz(request, pk):
    print(request.POST)
    return JsonResponse({"text":"works"})