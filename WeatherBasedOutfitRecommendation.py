import requests
import tkinter as tk
from tkinter import messagebox

# Replace with your OpenWeatherMap API key
API_KEY = 'your_openweather_api_key'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather?'

# Function to fetch weather data
def get_weather(city_name):
    complete_url = BASE_URL + "q=" + city_name + "&appid=" + API_KEY + "&units=metric"
    response = requests.get(complete_url)
    return response.json()

# Function to recommend an outfit based on temperature and weather conditions
def recommend_outfit(temp, weather):
    if weather == 'Rain' or weather == 'Drizzle':
        return "It's rainy! Wear a waterproof jacket and take an umbrella."
    elif weather == 'Snow':
        return "It's snowing! Wear a heavy coat, gloves, and boots."
    elif temp < 10:
        return "It's cold outside! Wear a heavy jacket, scarf, and a hat."
    elif temp < 20:
        return "It's cool! Wear a light jacket or a sweater."
    elif temp < 30:
        return "It's warm! Wear light clothing, like a t-shirt and jeans."
    else:
        return "It's hot! Wear shorts and a t-shirt."

# Function to fetch weather and update the GUI
def show_weather():
    city_name = city_entry.get()
    
    if not city_name:
        messagebox.showwarning("Input Error", "Please enter a city name!")
        return

    weather_data = get_weather(city_name)

    if weather_data['cod'] == 200:
        main_weather = weather_data['weather'][0]['main']
        temp = weather_data['main']['temp']
        
        weather_label.config(text=f"Weather: {main_weather}")
        temp_label.config(text=f"Temperature: {temp}°C")
        
        outfit = recommend_outfit(temp, main_weather)
        outfit_label.config(text=f"Recommended Outfit: {outfit}")
    else:
        messagebox.showerror("Error", "City not found. Please enter a valid city name.")

# Set up the Tkinter window
root = tk.Tk()
root.title("Weather-Based Outfit Recommender")

# Create and place the GUI components
city_label = tk.Label(root, text="Enter City Name:")
city_label.grid(row=0, column=0, padx=10, pady=10)

city_entry = tk.Entry(root, width=30)
city_entry.grid(row=0, column=1, padx=10, pady=10)

search_button = tk.Button(root, text="Get Weather", command=show_weather)
search_button.grid(row=0, column=2, padx=10, pady=10)

weather_label = tk.Label(root, text="Weather: ", font=('Arial', 12))
weather_label.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

temp_label = tk.Label(root, text="Temperature: ", font=('Arial', 12))
temp_label.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

outfit_label = tk.Label(root, text="Recommended Outfit: ", font=('Arial', 12))
outfit_label.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

# Run the Tkinter main loop
root.mainloop()