from django.shortcuts import render

# Create your views here.
def dashboard(request):
    return render(request, "home.html")

def quiz(request):
    return render (request, "quiz-page.html")
