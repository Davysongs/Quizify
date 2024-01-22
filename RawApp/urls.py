from django.urls import path
from . import views


urlpatterns = [
    path('sign/', views.register, name= "register"),
    path('login/', views.signin, name='login'),
    path('logout/', views.userlogout, name='logout'),
    path('', views.main, name="main"),
    path('home/', views.QuizListView.as_view() , name="home"),
    path('quiz/<int:pk>', views.quiz_view, name= "quiz"),
    path('quiz/<int:pk>/data', views.quiz_data, name ="quiz_data"),
]
