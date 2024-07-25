"""
Create a service to communicate with the FatSecret API.
"""
import requests
from requests.auth import HTTPBasicAuth
from django.conf import settings

class FatSecretAPI:
    """
    Service to communicate with Fatsecret API.
    """
    BASE_URL = 'https://platform.fatsecret.com/rest/server.api'
    TOKEN_URL = 'https://oauth.fatsecret.com/connect/token'

    def __init__(self):
        # Initialize with client ID and client secret from settings
        self.client_id = settings.FATSECRET_CLIENT_ID
        self.client_secret = settings.FATSECRET_CLIENT_SECRET
        # Obtain access token on initialization
        self.access_token = self.get_access_token()

    def get_access_token(self):
        """
        Obtain an access token using OAuth 2.0 client credentials flow.
        """
        data = {
            'grant_type': 'client_credentials',
        }
        auth = HTTPBasicAuth(self.client_id, self.client_secret)
        response = requests.post(self.TOKEN_URL, data=data, auth=auth)
        response_data = response.json()
        return response_data['access_token']

    def request(self, params):
        """
        Make a request to the Fatsecret API with the given parameters.
        """
        headers = {
            'Authorization': f'Bearer {self.access_token}',
        }
        response = requests.post(self.BASE_URL, headers=headers, data=params)
        return response.json()

    def search_food(self, query):
        """
        Search for food items matching the provided query.
        """
        params = {
            'method': 'foods.search',
            'format': 'json',
            'search_expression': query,
        }
        return self.request(params)
    
    def get_food_details(self, food_id):
        """
        Get details of the nutritional information of a food item of the given
        food id and return in a dictionary.
        """
        # Get food object of the provided food id
        params = {
            'method': 'food.get',
            'format': 'json',
            'food_id': food_id,
        }
        response = self.request(params)
        food = response.get('food')
        # Default get the first serving ID - Could be enhanced to display all serving options
        servings = food.get('servings').get('serving')
        serving = servings[0] if isinstance(servings, list) else servings
        
        return {
            'id': food_id,
            'name': food['food_name'],
            'calories': serving['calories'],
            'fat': serving['fat'],
            'protein': serving['protein'],
            'carbohydrate': serving['carbohydrate']
        }
