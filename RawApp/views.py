from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from rest_framework.response import Response
from django.contrib import messages
from RawApp.forms import SignForm #LogForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.views.generic import ListView
from .models import Quiz
from django.utils.decorators import method_decorator
from django.http import JsonResponse, Http404
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
        results = [ ]
        correct = None

        for q in questions:
            selected = request.POST.get(str(q))

            if selected  != "":
                sanswer = Answer.objects.filter(question = q)
                for ans in sanswer:
                    if selected == ans.text:
                        if ans.correct == True:
                            score +=1
                            correct_ans = ans.text
                    else:
                        if ans.correct:
                            correct_ans = ans.text
                results.append({str(q):{"Correct Answer":correct_ans, "Answered": selected}})
            else:
                results.append({str(q):"Not Answered"})

#calculate the user's score in percentage
        total = (score/quiz.quiz_length) * 100
        Result.objects.create(quiz= quiz, user = user, score = total) 
        print(quiz.pass_mark)
        if  total >= quiz.pass_mark:
            return JsonResponse({"passed":True, "score":total})

    return JsonResponse({"text":"works"})

@login_required(login_url= 'login')
def result(request,id):
    """View to show the result of a particular quiz"""
    #checking whether the user is trying to access another users result or not
    try:
        quiz = get_object_or_404(Quiz, pk=request.GET['id'])
        if request.user != quiz.creator and not request.user.is_superuser :
            raise Http404("No such quiz exists")
    except KeyError:
        quiz = Quiz.objects.get(pk=id)
        #getting all the results related to this quiz from database 
        resultee = Result.objects.filter(quiz=quiz).order_by('-created_at')[:5]
        context={'results':resultee,'quiz':quiz}
        return render(request,"result.html",context)
    result = Result.objects.get(quiz=quiz, user=request.user)
    context={'result':result,'quiz':quiz}
    return render(request,"result.detail.html",context)

def custom_404(request, exception):
    return render(request, '404.html', status=404)
