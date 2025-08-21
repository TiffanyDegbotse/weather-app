import requests
import os
from dotenv import load_dotenv
import streamlit as st

st.title("🌤️ Weather App")

# Load your API key from .env file
load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

def get_weather(city):
    """
    Fetch weather for the given city and print it nicely.
    """
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
    return response.json()
city=st.text_input("What city do you want information on?")

if st.button("Get weather results"):
    data=get_weather(city)
    # 5. Extract key info
    # #print(data)
    city_name = data["name"]
    temp = data["main"]["temp"]
    description = data["weather"][0]["description"]
    humidity=data["main"]["humidity"]
    # 6. Print
    st.write(f"In {city_name}, it is {temp}°C with {description} and humidity {humidity}.")


