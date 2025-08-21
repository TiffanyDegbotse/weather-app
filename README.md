# Weather CLI App

This project fetches weather information for a city using the OpenWeatherMap API and prints it in the command line.

## Setup

1. Clone the repository:
```bash
git clone <your-repo-url>
cd <repo-folder>

Create a .env file in the project root with your API key:

OPENWEATHER_API_KEY=your_api_key_here

Install dependencies (if using requests and python-dotenv):

pip install -r requirements.txt

Usage
Run the script:

python get_weather.py

Then type the city name when prompted.

###Streamlit app
# 🌤️ Weather App

This project fetches weather information for a city using the OpenWeatherMap API. It can be run in the command line or as a Streamlit web app. The Streamlit app allows you to enter a city name and view current weather details like temperature, humidity, and conditions with emojis, as well as interactive charts showing 5-day temperature and humidity trends.

To set up the project, first clone the repository with `git clone <your-repo-url>` and navigate into the folder with `cd <repo-folder>`. Create a `.env` file in the project root with your API key: `OPENWEATHER_API_KEY=your_api_key_here`. Install dependencies using `pip install -r requirements.txt`, which includes `streamlit`, `requests`, `python-dotenv`, and `pandas`.

You can run the app in the command line by executing `python get_weather.py` and typing the city name when prompted. To use the Streamlit web app, run `streamlit run app.py`. This will open a local web app in your browser where you can enter a city name, see the current weather, and view charts for temperature and humidity trends over the next 5 days. The app also includes emojis to represent weather conditions like clear, cloudy, or rainy skies, making it visually engaging.
