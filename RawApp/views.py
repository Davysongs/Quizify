from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from rest_framework.response import Response
from django.contrib import messages
from django.contrib.messages import get_messages
from RawApp.forms import SignForm #LogForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.generic import ListView
from .models import Quiz
from django.utils.decorators import method_decorator
from django.http import JsonResponse, Http404
from Questions.models import Question, Answer
from Results.models import Result
import datetime 
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
        return render(request, "login.html") 

# def get_message(request):
#     if request.method == "GET" and request.is_ajax():
#         # Retrieve messages from the storage
#         storage = get_messages(request)
#         # Convert messages to a list of dictionaries
#         messages_list = [{'message': message.message, 'extra_tags': message.tags} for message in storage]        # Return messages as JSON response
#         print(messages_list)
#         return JsonResponse({'messages': messages_list})



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
    if request.method == "GET":
        quiz = Quiz.objects.get(pk=pk)
        questions = []
        for data in quiz.getquestions():
            answers = []
            for a in data.get_answers():
                answers.append(a.text)
            questions.append({str(data):answers})
        # Get the current date and time
        current_datetime = datetime.datetime.now()
        # Convert the current date and time to an integer
        timestamp_integer = int(current_datetime.timestamp())
        # Function to generate random letters
        def generate_random_letters(length):
            letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            return ''.join(random.choice(letters) for _ in range(length))
        # Append two random letters to the integer
        quizID = str(timestamp_integer)+ str(pk) + generate_random_letters(2)
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
        Result.objects.create(quiz= quiz, user = user, score = total, result_id = quizID, question_ans = picked, answer_status = correct_status, status = verdict)
    else:
        return redirect("/home/")
    return JsonResponse({
        'message':"Done"
    })    

#get only the quiz results of the user
@login_required(login_url= 'login')
def results(request):
    if request.method == "GET":
        detail = request.GET.get('quizref')
        username = request.user.username
        userdata = User.objects.get(username = username)
        #to see only one specific result in detail after quiz has ended
        if detail != None and detail !="":
            try:
                redetail = Result.objects.get(result_id = detail)
                if redetail.user == userdata or userdata.is_staff:
                    #return html document that renders the persons result and performance 
                    return render (request, "result_detail.html",{"result":redetail})
                else:
                    message = "You are not permitted to view  other results, contact the admin for any complaints"
                    custom_404(request, message)
            except Result.DoesNotExist:
                # requested result does not exist
                message = "The result you requested to view does not exist"
                custom_404(request, message)
    #to see all previous user results in a specific quiz
        else:
            userobj = Result.objects.filter(user = userdata.id)
            return render(request, "result.html", {"resobj" : userobj})
    else:
        message = "You made an INVALID request"
        custom_404(request, message)
        

@login_required(login_url= 'login')
def result(request, pk):
    if request.method == "GET":
        username = request.user.username
        user = User.objects.get(username=username)
        uniresult = Result.objects.filter(quiz = pk , user = user )
        return render(request, "result.html",{"resobj":uniresult})
    else:
       message = "You made an INVALID request"
       custom_404(request, message)



