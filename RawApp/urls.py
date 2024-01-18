from django.urls import path
from . import views



urlpatterns = [
    path('sign/', views.SignUp.as_view(), name= "register"),
    path('login/', views.Login.as_view(), name='login'),
    path('login/', views.Logout.as_view(), name='logout'),
    path('', views.main, name="main"),
]
