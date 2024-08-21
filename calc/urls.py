from django.contrib import admin
from django.urls import path, include
from django.urls import path
from . import views

urlpatterns = [
path('admin/', admin.site.urls),
path('', views.home, name='home'),
]
urlpatterns=[
path('',views.home, name='home'),
path('dashboard/', views.dashboard, name='dashboard'),
path('user/<int:id>/', views.user_detail, name='user'),
path('add',views.enter, name='enter'),
]