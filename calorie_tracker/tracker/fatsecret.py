"""
Create a service to communicate with the FatSecret API.
"""
import requests
from requests.auth import HTTPBasicAuth
from django.conf import settings

class FatSecretAPI:
    BASE_URL = 'https://platform.fatsecret.com/rest/server.api'
    TOKEN_URL = 'https://oauth.fatsecret.com/connect/token'

    def __init__(self):
        self.client_id = settings.FATSECRET_CLIENT_ID
        self.client_secret = settings.FATSECRET_CLIENT_SECRET
        self.access_token = self.get_access_token()

    def get_access_token(self):
        data = {
            'grant_type': 'client_credentials',
        }
        auth = HTTPBasicAuth(self.client_id, self.client_secret)
        response = requests.post(self.TOKEN_URL, data=data, auth=auth)
        response_data = response.json()
        return response_data['access_token']

    def request(self, method, params):
        headers = {
            'Authorization': f'Bearer {self.access_token}',
        }
        response = requests.post(self.BASE_URL, headers=headers, data=params)
        print(response.json())
        return response.json()

    def search_food(self, query):
        params = {
            'method': 'foods.search',
            'format': 'json',
            'search_expression': query,
        }
        return self.request('POST', params)

    def get_food(self, food_id):
        params = {
            'method': 'food.get',
            'format': 'json',
            'food_id': food_id,
        }
        return self.request('POST', params)
    
    def get_food_details(self, food_id):
        """Returns nutritional information of a food_id as hashmap"""
        params = {
            'method': 'food.get',
            'format': 'json',
            'food_id': food_id,
        }
        response = self.request('POST', params)
        food = response.get('food')
        print(food)
        servings = food.get('servings').get('serving')
        serving = servings[0] if isinstance(servings, list) else servings # default get the first serving ID
        return {
            'name': food['food_name'],
            'calories': serving['calories'],
            'fat': serving['fat'],
            'protein': serving['protein'],
            'carbohydrate': serving['carbohydrate']
        }
