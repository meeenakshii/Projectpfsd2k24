# Generated by Django 5.1 on 2024-09-26 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0007_recipe_calories_per_100g_recipe_protein_per_100g'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='carbohydrates_per_100g',
            field=models.FloatField(default=30.0),
        ),
    ]
