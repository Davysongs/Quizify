from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from rest_framework.response import Response
from django.contrib import messages
from django.contrib.messages import get_messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from django.utils.decorators import method_decorator
from django.utils import timezone
from django.http import JsonResponse, Http404
from Questions.models import Question, Answer
from Results.models import Result
from RawApp.forms import SignForm
from RawApp.models import Quiz
from RawApp.middlewares import CustomException
import random
import ast

# Create your views here
#Home page 
class HomeView(ListView):
    model = Quiz
    template_name = "index.html"

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
                # Set a flag to indicate successful registration
                condition = True
                return render(request, "sign-up.html", {'condition': condition})
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


@login_required(login_url= 'login')
def save_quiz(request, pk):
    if request.is_ajax() and request.method == "POST":
        try:
            Result.objects.get(result_id =pk)
        except:
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
        total = ((score/quiz.quiz_length) * 100).__round__(2)
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
        if request.is_ajax():
            # Get the user's results
            page_num = request.GET.get('page')
            username = request.user.username
            userdata = User.objects.get(username = username)
            userobj = Result.objects.filter(user = userdata)
            # Paginate the results
            paginator = Paginator(userobj, 7)
            try:
                page = paginator.page(page_num)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                page = paginator.page(1)
            except EmptyPage:
                # If page is out of range, deliver last page of results.
                page = paginator.page(paginator.num_pages)

            # Serialize the results for JSON response

            result = []
            for i in page:
                res_data = Result.objects.get(result_id = i)
                reslist = {
                    "score":res_data.score,
                    "quiz":str(res_data.quiz), 
                    "resid":res_data.result_id,
                    "date":res_data.date.strftime('%Y-%m-%d %H:%M'),
                    "status":res_data.status
                }
                result.append(reslist)           
            return JsonResponse({"result":result, "total_pages": paginator.num_pages})
        else:        
            return render(request, "result.html")
    else: 
        raise CustomException("You Made an invalid request")
        

@login_required(login_url= 'login')
def quiz_result(request, pk):
    if request.method == "GET":
        username = request.user.username
        res_data = Result.objects.get(result_id = pk)
        if username == str(res_data.user):
            if request.is_ajax():
                result = []
                score = res_data.score
                quiz = str(res_data.quiz)
                resID = res_data.result_id
                date = res_data.date.strftime('%Y-%m-%d %H:%M')
                status = res_data.status
                result_list = ast.literal_eval(res_data.question_ans)
                ans = ast.literal_eval(res_data.answer_status )
                reslist = {"score":score,
                        "quiz":quiz, 
                        "resid":resID,
                        "date":date,
                        "status":status,
                        "pair": result_list,
                        "ans":ans
                        }
                result.append(reslist)
                return JsonResponse({
                    "result":result
                })
            else:
                return render(request, "result_detail.html",{"result":res_data})
        else:
           raise CustomException("You are not permitted to view this result, contact the admin for any complaints")
    else:
        raise CustomException("You Made an invalid request")
      



