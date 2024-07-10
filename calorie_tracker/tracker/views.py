from django.shortcuts import render
from .fatsecret import FatSecretAPI

def index(request):
    return render(request, "tracker/index.html")

def food_search(request):
    query = request.GET.get('query')
    fatsecret = FatSecretAPI()

    if query:
        results = fatsecret.search_food(query)
        foods = results.get('foods', {}).get('food', [])
    else:
        foods = []

    return render(request, 'tracker/food_search.html', {'foods': foods})

def food_detail(request, food_id):
    fatsecret = FatSecretAPI()
    food = fatsecret.get_food(food_id).get('food')
    serving = food.get('servings').get('serving')[0]
    
    return render(request, 'tracker/food_detail.html', {'food': food, 'serving': serving})