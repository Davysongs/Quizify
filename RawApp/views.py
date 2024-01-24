from django.shortcuts import render, redirect, HttpResponse
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
from Questions.models import Question, Answer
from Results.models import Result


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
            context = {"form" : form}
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get("username")
                messages.success(request, user + "your account was created successfully")
                return redirect('login')
            return render(request, "sign-up.html", context)
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
    # print(request.POST)
    if request.is_ajax():
        questions = []
        raw = request.POST
        data = dict(raw.lists())
        data.pop("csrfmiddlewaretoken")
        for key in data.keys():
            question = Question.objects.get(text = key)
            questions.append(question)
        user = request.user
        quiz = Quiz.objects.get(pk=pk)

        score = 0
        multiplier = 100/quiz.quiz_length
        results = [ ]
        correct = None

        for q in questions:
            selected = request.POST.get(str(q))
            print("Select"+selected)
            if selected  != "":
                sanswer = Answer.objects.filter(question = q)
                for ans in sanswer:
                    if selected == ans:
                        if ans.correct():
                            score +=1
                            correct_ans = ans.text
                    else:
                        if ans.correct():
                            correct_ans = ans.text
                results.append({str(q):{"Correct Answer":correct_ans, "Answered": selected}})
            else:
                results.append({str(q):"Not Answered"})
        scored = score * multiplier
        Result.objects.create(quiz= quiz, user = user, score =scored) 
        if scored >= quiz.pass_mark:
            return JsonResponse({"passed":True, "score":scored})

    return JsonResponse({"text":"works"})