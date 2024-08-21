from django.shortcuts import get_object_or_404, render
from .models import User
def home(request):
    return render(request, 'home.html', {'namep': 'PICKURHEALTH'})

def enter(request):
    n = request.POST.get('name', '')
    return render(request, 'enter.html', {'name': n})

def dashboard(request):
    users = User.objects.all()
    return render(request, 'dashboard.html', {'users': users})

def user_detail(request, id):
    user = get_object_or_404(User, id=id)
    return render(request, 'user_detail.html', {'user': user})

