from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.utils import timezone
from datetime import timedelta
from .fatsecret import FatSecretAPI
from .models import *
import json
from django.http import JsonResponse


def index(request):
    """Home page"""
    if request.method == "GET":
        return render(request, "tracker/index.html")
    return food_search(request)

def food_search(request):
    """Search for food"""
    query = request.POST.get('query')
    fatsecret = FatSecretAPI()

    if query:
        results = fatsecret.search_food(query)
        foods = results.get('foods', {}).get('food', [])
    else:
        foods = []

    return render(request, 'tracker/food_search.html', {'query': query, 'foods': foods})

def food_detail(request, food_id):
    """Displays details of a food based on the food_id"""
    if request.method == "GET":
        fatsecret = FatSecretAPI()
        food = fatsecret.get_food_details(food_id)
        return render(request, 'tracker/food_detail.html', {'food': food})
    return save_entry(request)
    # else:
    #     """Saves food entry to the user"""
    #     food_entry = FoodEntry(
    #         user = request.user,
    #         food_id = request.POST["food_id"],
    #         name = request.POST["food_name"],
    #         calories = request.POST["calories"],
    #         fat = request.POST["fat"],
    #         protein = request.POST["protein"],
    #         carbohydrates = request.POST["carbohydrate"],
    #     )
    #     food_entry.save()
    #     return HttpResponseRedirect(reverse("food_search")) # could design a JS pop up window


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "tracker/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "tracker/login.html")

@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "tracker/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "tracker/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "tracker/register.html")
    
@login_required
def save_entry(request):
    """Saves food entry to the user"""
    if request.method == 'POST':
        data = json.loads(request.body)
        food_entry = FoodEntry(
            user=request.user,
            food_id=data["food_id"],
            name=data["food_name"],
            calories=data["calories"],
            fat=data["fat"],
            protein=data["protein"],
            carbohydrates=data["carbohydrates"],
            date=timezone.now()  # Assuming you want to save with the current date
        )
        food_entry.save()
        return JsonResponse({
            'status': 'success',
            'message': f"{data['food_name']} has been added to your profile"
        })
    else:
        return JsonResponse({
            'status': 'error',
            'message': 'Invalid request method'
        }, status=400)

@login_required
def my_profile(request):
    # Get the user's calorie data in a week
    today = timezone.now().date() - timedelta(days=1) # adjust for naive timezone
    past_week = today - timedelta(days=7)
    weekly_entries = FoodEntry.objects.filter(user=request.user, date__gte=past_week)
    weekly_entries.order_by('-date')

    # Calculate remaining calories for today
    goal = 2000
    today_entries = FoodEntry.objects.filter(user=request.user, date=today)
    today_calories = sum(float(entry.calories) for entry in today_entries)
    remaining_calories = goal - today_calories
    
    return render(request, "tracker/my_profile.html", {
        'weekly_entries': weekly_entries,
        'remaining_calories': remaining_calories,
        'goal': goal,
    })