from django import forms
from .models import FoodEntry

class FoodEntryForm(forms.ModelForm):
    class Meta:
        model = FoodEntry
        fields = ['name', 'calories', 'fat', 'protein', 'carbohydrates']
