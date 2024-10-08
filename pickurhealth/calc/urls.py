from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginPage, name='login'),  # Set the default path to the login page
    path('home/', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('user/<int:id>/', views.user_detail, name='user'),
    path('add/', views.enter, name='enter'),
    path('quiz/', views.quiz_view, name='quiz'),
    path('quiz/submit/', views.submit_quiz, name='submit_quiz'),
    path('recipes/', views.recipes, name='recipes'), 
    path('recipe/<int:id>/', views.recipe_detail, name='recipe_detail'), 
    path('register/', views.registerPage, name='register'), 
    path('logout/', views.logoutPage, name='logout'),  # Corrected logout view
    path('calendar/', views.performance_calendar, name='performance_calendar'),
    path('calendar/<int:year>/<int:month>/', views.performance_calendar, name='performance_calendar_by_month'),
    path('add_task/', views.add_task, name='add_task'),
    path('complete_task/<int:task_id>/', views.complete_task, name='complete_task'),  # Added task_id parameter for completion
    path('add_event/', views.add_event, name='add_event'),
]
