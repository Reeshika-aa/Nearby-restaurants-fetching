## How to Run This Project

1. Install Python  
   Ensure Python 3.7 or higher is installed. Download it from [python.org](https://www.python.org/).

2. Download the Project  
   - Clone the repository:  
   - git clone https://github.com/Reeshika-aa/Nearby-restaurants-fetching.git
   - Or download and extract the `.zip` file.

3. Install Libraries  
   Open a terminal in the project folder and run:  
   `pip install pandas,  chardet , and requests`

4. Set Up OpenWeather API (Optional)  
   - Create an account at [OpenWeather](https://openweathermap.org/) and get your API key.
   - Add the API key to the script where `api_key = "your_api_key_here"` is mentioned.

5. Run the Project  
   In the terminal, run:  
   `python app.py`
   store the index.html in tmeplates folder

6. View Output  
   Open your browser and go to:  
   `http://localhost:5000`  
  
### Where to Store Files

- HTML File: Store your `index.html` in the templates folder. Flask will automatically find and render it.


### How the Project Works

1. Weather and Busy Times:  
   Displays weather, busy status of the village, and menus of nearby restaurants.

2. Price Prediction:  
   Adjusts prices based on weather or busy times using a simple rule-based system.



For Real Weather Data (Optional):
1. Sign Up for OpenWeather API:  
   Get your API key from [OpenWeather](https://openweathermap.org/).
   
2. Fetch Weather:  
   Use this code to get the current weather:
CODE:
   import requests
   def fetch_weather(city_name, api_key):
       base_url = "https://api.openweathermap.org/data/2.5/weather"
       params = {"q": city_name, "appid": api_key, "units": "imperial"}
       response = requests.get(base_url, params=params)
       return response.json() if response.status_code == 200 else None

