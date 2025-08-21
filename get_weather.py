import requests
import os
from dotenv import load_dotenv

# Load your API key from .env file
load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

def get_weather():
    """
    Fetch weather for the given city and print it nicely.
    """
    city=input("Which city do you want information on?")
    # 1. Create the API endpoint URL
    url = "https://api.openweathermap.org/data/2.5/weather"
    
    # 2. Set query parameters
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"  # temperature in Celsius
    }
    
    # 3. Make the request
    response = requests.get(url, params=params)
    
    # 4. Parse JSON
    data = response.json()
    
    # 5. Extract key info
    #print(data)
    city_name = data["name"]
    temp = data["main"]["temp"]
    description = data["weather"][0]["description"]
    humidity=data["main"]["humidity"]
    
    # 6. Print
    print(f"In {city_name}, it is {temp}°C with {description} and humidity {humidity}.")

# Try it
get_weather()
