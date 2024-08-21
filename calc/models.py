from django.db import models

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
