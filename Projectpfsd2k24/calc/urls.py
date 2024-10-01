from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth import authenticate, login, logout 
from django.contrib import messages 
from django.contrib.auth.decorators import login_required 
from django.views.decorators.cache import cache_control

urlpatterns = [
    path('', views.loginPage, name='login'),
    path('home/', views.home, name='home'),
    path('login/', views.loginPage, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('user/<int:id>/', views.user_detail, name='user'),
    path('add/', views.enter, name='enter'),
    path('quiz/', views.quiz_view, name='quiz'),
    path('quiz/submit/', views.submit_quiz, name='submit_quiz'),
    path('recipes/', views.recipes, name='recipes'), 
    path('recipe/<int:id>/', views.recipe_detail, name='recipe_detail'), 
    path('register/', views.registerPage, name='register'), 
    path('logout/',views.logoutPage, name='logout'),  # Corrected logout view
]

