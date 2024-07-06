"""
Create a service to communicate with the FatSecret API.
"""

import requests
from requests_oauthlib import OAuth1
from requests_oauthlib import OAuth1Session
from django.conf import settings
import time
import uuid

class FatSecretAPI:
    BASE_URL = 'https://platform.fatsecret.com/rest/server.api'

    def __init__(self):
        self.consumer_key = settings.FATSECRET_CONSUMER_KEY
        self.consumer_secret = settings.FATSECRET_CONSUMER_SECRET

    def request(self, params):
        oauth = OAuth1Session(self.consumer_key, client_secret=self.consumer_secret, signature_method='HMAC-SHA1')
        # params['oauth_signature_method'] = 'HMAC-SHA1'
        # params['oauth_consumer_key'] = self.consumer_key
        # params['oauth_nonce'] = uuid.uuid4().hex
        # params['oauth_timestamp'] = time.time()

        r = oauth.post(self.BASE_URL, data=params)
        print(r.json())

        return r.json()

    def search_food(self, query):
        params = {
            'method': 'foods.search',
            'format': 'json',
            'search_expression': query,
        }
        return self.request(params)

    def get_food(self, food_id):
        params = {
            'method': 'food.get',
            'format': 'json',
            'food_id': food_id,
        }
        return self.request(params)