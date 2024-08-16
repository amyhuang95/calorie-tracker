# Calorie Tracker
This project is a nutrition tracking web application built using Django and FatSecret API. It allows users to search for food items, retrieve their nutritional information, and log their daily food intake into their personal profiles.

## Features
- **User Authentication**: Users can register, log in, and save their personal nutrition entries.
- **Food Search**: Integration with the FatSecret API allows users to search for food items and retrieve detailed nutritional information.
- **Nutrition Calculation**: Dynamic adjustment of nutrition values based on the number of servings provided by user.
- **Food Logging**: Users can save food entries (along with their nutrition details) into their personal profiles.
- **Personalized Dashboard**: Users can view a summary of their daily and weekly calorie intake.

## Tech Stack
- **Backend**: Python, Django
- **Database**: SQLite
- **Frontend**: HTML, CSS & Bootstrap, JavaScript
- **API**: FatSecret API

## Set up
1. Clone the repository.
2. Create and activate a virtual environment.
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```
4. Install dependencies. 
   ```
   pip install -r requirements.txt
   ```
5. FatSecret API requires access token to use. Please refer to [documentation](https://platform.fatsecret.com/docs/guides/authentication/oauth2). After obtaining Fatsecret API credentials, create a `.env` file in the root directory and include below:
   ```
   FATSECRET_CLIENT_ID="YOUR CLIENT ID"
   FATSECRET_CLIENT_SECRET="YOUR CLIENT SECRET"
   ```
6. Set up database.
   ```
   python manage.py migrate
   ```
7. Run server.
   ```
   python manage.py runserver
   ```
8. Access the application by opening a web browser and going to `http://127.0.0.1:8000`
