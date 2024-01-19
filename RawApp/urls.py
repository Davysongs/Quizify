from django.urls import path,include
from . import views



urlpatterns = [
    path('sign/', views.register, name= "register"),
    path('login/', views.signin, name='login'),
    path('logout/', views.userlogout, name='logout'),
    path('', views.main, name="main"),
    path('home', views.home , name="home"),
]
