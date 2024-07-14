from django.urls import path
from . import views

urlpatterns= [
    path("", views.index, name="index"),
    path("food-search/", views.food_search, name="food_search"),
    path("food-detail/<str:food_id>", views.food_detail, name="food_detail"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("save-entry/", views.save_entry, name="save_entry"),
]
