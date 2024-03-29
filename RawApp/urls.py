from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.register, name= "register"),
    path('login/', views.signin, name='login'),
    path('logout/', views.userlogout, name='logout'),
    path('', views.HomeView.as_view(), name="main"),
    path('home/', views.QuizListView.as_view() , name="home"),
    path('quiz/<int:pk>', views.quiz_view, name= "quiz"),
    path('quiz/<int:pk>/data', views.quiz_data, name ="quiz_data"),
    path('quiz/<int:pk>/save/', views.save_quiz, name ="save_quiz"),
    path('results/', views.results, name= "results"),
    path('results/<str:pk>', views.quiz_result, name= "results"),     
]
