from django.shortcuts import get_object_or_404, render, redirect
from .models import User, Recipe, Question  # Import your models
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.utils import timezone
import calendar
from datetime import datetime
from calendar import monthcalendar, month_name

# Home view
def home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        return render(request, 'home.html', {'namep': 'PICKURHEALTH'})

# Enter view
def enter(request):
    n = request.POST.get('name', '')
    return render(request, 'enter.html', {'name': n})

# Dashboard view
def dashboard(request):
    if not request.user.is_authenticated:
        messages.error(request, "You must be logged in to access the dashboard.")
        return redirect('login')
    users = User.objects.all()
    return render(request, 'dashboard.html', {'users': users})

# User detail view
def user_detail(request, id):
    user = get_object_or_404(User, id=id)
    return render(request, 'user_detail.html', {'user': user})

# Submit quiz view
def submit_quiz(request):
    # Assuming you are getting the questions from your database
    questions = Question.objects.all()  # or however you fetch your questions
    user_answers = request.POST.getlist('user_answers')  # Adjust based on how you capture answers
    # other logic
    return render(request, 'results.html', {'questions': questions, 'user_answers': user_answers})

def quiz_results(request):
    user_answers = {}
    for question_id in range(1, 14):  # Assuming there are 13 questions
        user_answers[f'question{question_id}'] = request.POST.get(f'question{question_id}')
    
    # Example analysis based on answers
    productivity = None
    goal = None
    sleep_hours = None
    meal_timing = None
    activity_preference = None
    relaxation_time = None

    # For question 1: Wake-up time
    wake_up_time = user_answers.get('question1')
    
    # For question 2: Typical shift hours
    shift_hours = user_answers.get('question2')

    # For question 3: Sleep hours
    sleep_hours = user_answers.get('question3')
    
    # For question 4: Physical activity preference
    activity_preference = user_answers.get('question4')

    # For question 5: Goals
    goal = user_answers.get('question5')

    # For question 6: Evening enjoyment preference
    evening_enjoyment = user_answers.get('question6')

    # For question 10: Time-management challenge
    time_management_challenge = user_answers.get('question10')

    # For question 11: Relaxation time
    relaxation_time = user_answers.get('question11')

    # Fetching all questions
    questions = Question.objects.all()

    context = {
        'questions': questions,
        'user_answers': user_answers,
        'wake_up_time': wake_up_time,
        'shift_hours': shift_hours,
        'sleep_hours': sleep_hours,
        'activity_preference': activity_preference,
        'goal': goal,
        'evening_enjoyment': evening_enjoyment,
        'time_management_challenge': time_management_challenge,
        'relaxation_time': relaxation_time,
    }
    
    return render(request, 'results.html', context)


# Recipes view
def recipes(request):
    recipe_list = Recipe.objects.all()
    return render(request, 'recipes.html', {'recipes': recipe_list})

# Recipe detail view
def recipe_detail(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    return render(request, 'recipe_detail.html', {'recipe': recipe})

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')

    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully. You can now log in!')
            return redirect('login')

    context = {'form': form}
    return render(request, 'register.html', context)

# Validate password function
def validate_password(password):
    min_length = 8
    has_letters = any(c.isalpha() for c in password)
    has_numbers = any(c.isdigit() for c in password)
    has_special_chars = any(c in "!@#$%^&*(),.?\":{}|<>" for c in password)
    
    return (len(password) >= min_length and
            has_letters and
            has_numbers and
            has_special_chars)

# Login view
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password")
    
    return render(request, 'login.html')

# Logout view
def logoutPage(request):
    logout(request)
    return redirect('login')

# Quiz view
def quiz_view(request):
    return render(request, 'quiz.html')

# Function to get month data
def get_month_data(year, month):
    weeks = calendar.monthcalendar(year, month)
    month_name = calendar.month_name[month]
    return {
        'year': year,
        'month': month,
        'month_name': month_name,
        'weeks': weeks,
    }

# Performance calendar view
def performance_calendar(request):
    # Get the current date
    today = datetime.today()
    
    # Get 'month' and 'year' from the GET request, defaulting to the current month and year
    current_month = int(request.GET.get('month', today.month))
    current_year = int(request.GET.get('year', today.year))

    # Prepare data for all 12 months of the current year
    months = []
    for month in range(1, 13):
        month_data = {
            'month': month,
            'month_name': month_name[month],
            'year': current_year,
            'weeks': monthcalendar(current_year, month),  # Get the month calendar
        }
        months.append(month_data)

    context = {
        'months': months,
        'current_month': current_month,
        'current_year': current_year,
        'today_date': today,
        'important_events': [],  # Your logic to get events
        'current_month_index': current_month - 1,
    }

    return render(request, 'performance_calendar.html', context)

# Temporary in-memory task list
tasks = []

# Add task view
def add_task(request):
    if request.method == 'POST':
        task_name = request.POST.get('task_name')
        if task_name and request.user.is_authenticated:
            task = {
                'id': len(tasks) + 1,
                'name': task_name,
                'completed': False,
                'user': request.user.username,
                'date_added': timezone.now().date()
            }
            tasks.append(task)
        return redirect('performance_calendar')

    return redirect('performance_calendar.html')

# Complete task view
def complete_task(request, task_id):
    if request.method == 'POST':
        for task in tasks:
            if task['id'] == int(task_id):
                task['completed'] = not task['completed']
                break
        return redirect('performance_calendar.html')
def add_event(request):
    if request.method == 'POST':
        title = request.POST.get('title')  # Handle data without the model
        # Process the event data without saving to the database


from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    user = request.user
    return render(request, 'profile.html', {'user': user})

from django.contrib.auth.forms import UserChangeForm

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserChangeForm(instance=request.user)

    return render(request, 'edit_profile.html', {'form': form})



