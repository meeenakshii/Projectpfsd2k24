from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models import Q

class User(models.Model):
    CATEGORY_CHOICES = (
        ('Weightloss', 'Weightloss'),
        ('Weightgain', 'Weightgain'),
        ('Get-fit', 'Getfit'),
        ('Lifestyle', 'Lifestyle'),
        ('Recovery', 'Recovery'),
    )

    name = models.CharField(max_length=300, null=True)
    age = models.CharField(max_length=300, null=True)
    height = models.CharField(max_length=300, null=True)
    weight = models.CharField(max_length=300, null=True)
    dob = models.DateField(null=True)
    date = models.DateTimeField(null=True)
    category = models.CharField(max_length=300, choices=CATEGORY_CHOICES, null=True)

    def __str__(self):
        return self.name

class Type(models.Model):
    name = models.CharField(max_length=300, null=True)
    
    def __str__(self):
        return self.name

# models.py
from django.db import models

class Question(models.Model):
    question = models.CharField(max_length=255)

    def __str__(self):
        return self.question

class Option(models.Model):
    question = models.ForeignKey(Question, related_name='options', on_delete=models.CASCADE)
    option_text = models.CharField(max_length=255)

    def __str__(self):
        return self.option_text


from django.db import models

class Recipe(models.Model):
    name = models.CharField(max_length=255, default="Unnamed Recipe")
    ingredients = models.TextField()
    cooking_time = models.IntegerField(default=30)  # In minutes
    servings = models.IntegerField(default=1)
    category = models.CharField(max_length=100, default='Uncategorized')
    process = models.TextField(default="No process provided")
    image = models.ImageField(upload_to='recipe_images/', blank=True, null=True)
    protein = models.FloatField(default=0.0)  # Protein content in grams
    carbohydrates = models.FloatField(default=0.0)  # Carbohydrate content in grams
    calories = models.IntegerField(default=0)   # Approximate calories per 100g


    def __str__(self):
        return self.name

from django.db import models
from django.contrib.auth.models import User  # If events are linked to users

class Event(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  # Optional user association

    def __str__(self):
        return f"{self.name} on {self.date}"
