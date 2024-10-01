from django.shortcuts import get_object_or_404, render
from .models import User
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def home(request):
        if not request.user.is_authenticated:
            return redirect('login')
        else:
            return render(request, 'home.html', {'namep': 'PICKURHEALTH'})

def enter(request):
    n = request.POST.get('name', '')
    return render(request, 'enter.html', {'name': n})

def dashboard(request):
    if not request.user.is_authenticated:
        messages.error(request, "You must be logged in to access the dashboard.")
        return redirect('login')  # Redirect to login if not authenticated

    # If the user is authenticated, show the dashboard
    users = User.objects.all()
    return render(request, 'dashboard.html', {'users': users})


def user_detail(request, id):
    user = get_object_or_404(User, id=id)
    return render(request, 'user_detail.html', {'user': user})


def submit_quiz(request):
    questions = [
        {'id': 1, 'question': 'What time do you usually start work or your daily tasks?', 'options': ['A) Before 7 AM', 'B) 7 AM - 9 AM', 'C) 9 AM - 11 AM', 'D) After 11 AM']},
        {'id': 2, 'question': 'How many hours do you typically work each day?', 'options': ['A) Less than 4 hours', 'B) 4-6 hours', 'C) 6-8 hours', 'D) More than 8 hours']},
        {'id': 3, 'question': 'Are you more productive in the morning or evening?', 'options': ['A) Morning', 'B) Afternoon', 'C) Evening', 'D) I don’t have a specific time']},
        {'id': 4, 'question': 'What is your primary professional goal for the next year?', 'options': ['A) Getting a promotion', 'B) Switching careers', 'C) Improving skills or education', 'D) Starting my own business']},
        {'id': 5, 'question': 'How do you prefer to structure your workday?', 'options': ['A) Block scheduling with set tasks', 'B) Flexible with to-do lists', 'C) A mix of both', 'D) I go with the flow']},
        {'id': 6, 'question': 'How do you like to unwind after work?', 'options': ['A) Exercise or outdoor activities', 'B) Socializing with friends or family', 'C) Hobbies or personal projects', 'D) Watching TV or playing video games']},
        {'id': 7, 'question': 'How often do you set personal goals?', 'options': ['A) Daily', 'B) Weekly', 'C) Monthly', 'D) Rarely']},
        {'id': 8, 'question': 'How do you typically prepare for the next day?', 'options': ['A) Planning my schedule the night before', 'B) Writing a to-do list', 'C) I don’t usually prepare', 'D) I like to keep it spontaneous']},
        {'id': 9, 'question': 'Do you prefer working alone or in a team?', 'options': ['A) Alone', 'B) In a small team', 'C) In larger teams', 'D) It depends on the task']},
        {'id': 10, 'question': 'What would you like to improve in your daily routine?', 'options': ['A) Time management', 'B) Work-life balance', 'C) Health and fitness', 'D) Skill development']},
        {'id': 11, 'question': 'What time of day do you usually feel most creative?', 'options': ['A) Early morning', 'B) Late morning', 'C) Afternoon', 'D) Evening or night']},
        {'id': 12, 'question': 'What would you like to incorporate more into your daily routine?', 'options': ['A) More breaks', 'B) Mindfulness or meditation', 'C) Physical activity', 'D) Social interactions']},
        {'id': 13, 'question': 'How often do you reflect on your work-life balance?', 'options': ['A) Regularly', 'B) Occasionally', 'C) Rarely', 'D) I don’t think about it']}
    ]

    user_answers = {}
    for question in questions:
        user_answers[question['id']] = request.POST.get(f'question{question["id"]}')

    # Create context to pass to the template
    context = {
        'user_answers': user_answers,
        'questions': questions,
    }

    # Render the results page with the context
    return render(request, 'results.html', context)


from django.shortcuts import render, get_object_or_404
from .models import Recipe 

def recipes(request):
    recipe_list = Recipe.objects.all()

    return render(request, 'recipes.html', {'recipes': recipe_list})

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

def validate_password(password):
    # Example validation rules: adjust as necessary
    min_length = 8
    has_letters = any(c.isalpha() for c in password)
    has_numbers = any(c.isdigit() for c in password)
    has_special_chars = any(c in "!@#$%^&*(),.?\":{}|<>" for c in password)
    
    return (
        len(password) >= min_length and
        has_letters and
        has_numbers and
        has_special_chars
    )


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')  # Redirect to home if already logged in
    
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)  # Authenticate user
        
        if user is not None:
            login(request, user)  # Log in the user if authentication is successful
            return redirect('home')  # Redirect to home after login
        else:
            messages.error(request, "Invalid username or password")
    
    return render(request, 'login.html')


def logoutPage(request):
    logout(request)
    return redirect('login')

def quiz_view(request):
    return render(request, 'quiz.html')
