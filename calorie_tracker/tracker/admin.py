"""
Register models in admin dashboard.
"""

from django.contrib import admin
from .models import *

@admin.register(FoodEntry)
class FoodEntryAdmin(admin.ModelAdmin):
    list_display = ('name', 'calories', 'date')
    search_fields = ('name',)
