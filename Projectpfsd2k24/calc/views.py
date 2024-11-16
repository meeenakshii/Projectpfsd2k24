from django.shortcuts import get_object_or_404, render, redirect
from .models import User, Recipe, Event  # Import your models
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.utils import timezone
from datetime import datetime
from calendar import monthcalendar, month_name
import calendar

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
    questions = [
        {'id': 1, 'question': 'What time do you usually start work or your daily tasks?', 'options': ['A) Before 7 AM', 'B) 7 AM - 9 AM', 'C) 9 AM - 11 AM', 'D) After 11 AM']},
        # Add more questions as needed
    ]
    user_answers = {}
    for question in questions:
        user_answers[question['id']] = request.POST.get(f'question{question["id"]}')

    context = {
        'user_answers': user_answers,
        'questions': questions,
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

# Registration view
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
    today = datetime.today()
    current_month = today.month
    current_year = today.year

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

# Add event view
def add_event(request):
    if request.method == 'POST':
        event_name = request.POST.get('event_name')
        event_date = request.POST.get('event_date')

        # Check if both event name and date are provided
        if event_name and event_date:
            # Add the event to the context (you might need to implement a way to store events in session or similar)
            # Here, we are assuming you have a way to keep track of events for the current session.
            if 'important_events' not in request.session:
                request.session['important_events'] = []
            request.session['important_events'].append({
                'name': event_name,
                'date': event_date
            })
            request.session.modified = True  # Mark the session as modified

            # Redirect to the calendar view
            return redirect('performance_calendar')  # Change this to your calendar view name

    # If the request is GET or if validation fails, render the calendar with existing events
    return render(request, 'performance_calendar.html', {
        'important_events': request.session.get('important_events', []),  # Pass events to the template
    })  # Redirect in case of GET or invalid data
