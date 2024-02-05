from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from rest_framework.response import Response
from django.contrib import messages
from django.contrib.messages import get_messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.generic import ListView
from django.utils.decorators import method_decorator
from django.utils import timezone
from django.http import JsonResponse, Http404
from Questions.models import Question, Answer
from Results.models import Result
from RawApp.forms import SignForm
from RawApp.models import Quiz

import random


# Create your views here.

#error handler
def custom_404(request, exception):
    return render(request, '404.html', {'error_message': exception})


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
                messages.add_message(request,messages.SUCCESS, user + " your account was created successfully")
                stored_messages = messages.get_messages(request)

    # Convert messages to a list of dictionaries
                messages_list = [{'message': message.message, 'extra_tags': message.tags} for message in stored_messages]
                stored_messages.used = False
                request.session['data_to_pass'] = messages_list
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

        #send confirmation data to login page
        if request.method == "GET" and request.is_ajax():
            # Return JSON response for AJAX requests
            received_data = request.session.get('data_to_pass')
            return JsonResponse({'messages': received_data})
        return render(request, "login.html")



#Logout
def userlogout(request):
    logout(request)
    return redirect('home')

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
    if request.method == "GET":
        quiz = Quiz.objects.get(pk=pk)
        questions = []
        for data in quiz.getquestions():
            answers = []
            for a in data.get_answers():
                answers.append(a.text)
            questions.append({str(data):answers})
        # Get the current date and time as quiz id
        current_datetime = timezone.now()
        datestring = current_datetime.strftime('%m%d%H%M%S')
        # to generate random letters
        letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        unique = ''.join(random.choice(letters) for _ in range(2))
        # Append two random letters to the integer
        quizID = str(unique)+ datestring
        return JsonResponse({
            'data':questions,
            'time':quiz.time,
            'qid': quizID
        })
    else:
        return redirect("/home/")

@login_required(login_url= 'login')
def save_quiz(request, pk):
    if request.is_ajax() and request.method == "POST":
        quizID = request.GET.get("content")
        questions = []
        data = dict(request.POST.lists())
        data.pop("csrfmiddlewaretoken")
        for key in data.keys():
            question = Question.objects.get(text = key)
            questions.append(question)
        user = request.user
        quiz = Quiz.objects.get(pk=pk)

        score = 0
        picked = [ ]
        correct_status = [ ]

        for q in questions:
            selected = request.POST.get(str(q))

            if selected  != "":
                sanswer = Answer.objects.filter(question = q)
                for ans in sanswer:
                    if selected == ans.text:
                        if ans.correct:
                            score +=1
                            correct = "True"
                    else:
                        if ans.correct:
                            #ANS.TEXT IS THE CORRECT ANSWER
                            correct = "False"
                correct_status.append(correct)
                picked.append({str(q):selected})
            else:
                picked.append({str(q):"Not Answered"})
                correct_status.append("False")

        #calculate the user's score in percentage
        total = (score/quiz.quiz_length) * 100
        if  total >= quiz.pass_mark:
            verdict = "Passed"
        else:
            verdict = "Failed"
        Result.objects.create(quiz= quiz, user = user, score = total, result_id = quizID, 
                              question_ans = picked, answer_status = correct_status, status = verdict)
    else:
        return redirect("home")
    return JsonResponse({
        'message':"Done"
    })    

#get only the quiz results of the user
@login_required(login_url= 'login')
def results(request):
    if request.method == "GET":
        return render(request, "result.html")
    else:
        message = "You made an INVALID request"
        custom_404(request, message)
        

@login_required(login_url= 'login')
def quiz_result(request, pk):
    if request.method == "GET":
        username = request.user.username
        try:
            userdata = User.objects.get(username = username)
            return render(request, "result.html")
        except :
            message = "You are not permitted to view  other results, contact the admin for any complaints"
            custom_404(request, message)
    else:
       message = "You made an INVALID request"
       custom_404(request, message)

       

@login_required(login_url='login')
def get_results(request, pk):
    if request.method == "GET" and request.is_ajax():
            try:
                redetail = Result.objects.get(result_id = pk)
                return JsonResponse({
                    "result":redetail
                })
            except Result.DoesNotExist:
                # requested result does not exist
                message = "The result you requested to view does not exist"
                custom_404(request, message)

@login_required(login_url='login')
def get_results(request):
    #to see all previous user results in a specific user
    username = request.user.username
    userdata = User.objects.get(username = username)
    userobj = Result.objects.filter(user = userdata.id)
    return JsonResponse({
        "result":userobj
    })
