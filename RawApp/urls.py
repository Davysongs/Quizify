from django.urls import path
from . import views
from .forms import SignForm

urlpatterns = [
    #path('signup/', views.register, name='register'),
    path('sign/', views.Register.as_view(), name= "register"),
    path('login/', views.login, name='login'),
    path('', views.main, name="main"),
    path('quiz', views.test )
]
