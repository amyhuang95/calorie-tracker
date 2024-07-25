'''
Data models for food entry.
'''
from django.db import models
from django.contrib.auth.models import User


class FoodEntry(models.Model):
    """
    Food entry data model. 
    user: default user object
    food_id: food id in Fatsecret API
    name: food name
    calories: amount of calories in the food
    protein: amount of protein in the food
    carbohydrates: amount of carbohydrates in the food
    date: creation date
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food_id = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    calories = models.DecimalField(max_digits=6, decimal_places=2)
    fat = models.DecimalField(max_digits=6, decimal_places=2)
    protein = models.DecimalField(max_digits=6, decimal_places=2)
    carbohydrates = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        """Display the entry as a string"""
        return f"{self.name} - {self.calories} calories"