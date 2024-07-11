from django.contrib import admin
from .models import FoodEntry, NutritionalInformation

@admin.register(FoodEntry)
class FoodEntryAdmin(admin.ModelAdmin):
    list_display = ('name', 'calories', 'date')
    search_fields = ('name',)

@admin.register(NutritionalInformation)
class NutritionalInformationAdmin(admin.ModelAdmin):
    list_display = ('food_entry', 'nutrient_name', 'amount')
    search_fields = ('nutrient_name',)
