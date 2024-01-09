from django.shortcuts import render
from .models import User
import requests
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from RawApp.forms import SignForm, LogForm
from formtools.wizard.views  import SessionWizardView


# Create your views here.
#signup

class Register(SessionWizardView):
    form_list = [SignForm]
    template_name = "log.html"
    def done (self, from_list, **kwargs):
        return Response("form submitted")

# def register (request):
#     return render(request, "sign-up.html")

#login 
def login (request):
    log_info = LogForm()
    if request.method == "POST":
        u_email = request.POST.get("u_email")
        u_password = request.POST.get("u_password")
        log_info = LogForm(request.POST)
        if log_info.is_valid():
            search = request.query_params.get(u_email)
    context = {"form": log_info}
    return render(request, "login.html", context)    

def main(request):
    return render(request, "index.html")
def test(request):
    quiz_name ={"text":"Agriculture"}
    user_name = {"text": "Davido"} 
    return render(request, "quiz-page.html", quiz_name, ) 