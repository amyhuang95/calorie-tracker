from django.db import models
from django.contrib.auth.models import User
from users.models import CustomUser as User

class FoodEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    calories = models.DecimalField(max_digits=6, decimal_places=2)
    fat = models.DecimalField(max_digits=6, decimal_places=2)
    protein = models.DecimalField(max_digits=6, decimal_places=2)
    carbohydrates = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.calories} calories"

class NutritionalInformation(models.Model):
    food_entry = models.ForeignKey(FoodEntry, related_name='nutritional_info', on_delete=models.CASCADE)
    nutrient_name = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.nutrient_name} - {self.amount}"
