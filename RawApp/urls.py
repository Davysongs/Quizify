from django.urls import path
from . import views



urlpatterns = [
    path('sign/', views.register, name= "register"),
    path('login/', views.login, name='login'),
    path('', views.main, name="main"),
]
