from django.urls import path
from . import views

urlpatterns= [
    path("", views.index, name="index"),
    path("food-search/", views.food_search, name="food_search"),
    path("food-detail/<str:food_id>", views.food_detail, name="food_detail"),
]
