# Weather CLI App

A simple command-line application that fetches the current weather for any city using the OpenWeatherMap API. The app accepts city input from the user and displays temperature in Celsius, humidity, and a brief weather description.

## Setup and Usage

1. Clone the repository and navigate into the project folder:
   git clone <your-repo-url>
   cd <repo-folder>

2. Create a `.env` file in the project root with your API key:
   OPENWEATHER_API_KEY=your_api_key_here

3. Install the required Python packages:
   pip install -r requirements.txt

4. Run the script and follow the prompt to enter a city name:
   python get_weather.py

## Notes

- Ensure your `.env` file is listed in `.gitignore` so your API key is not exposed on GitHub.  
- You can customize the CLI output or extend the app to include additional weather information from the API.
