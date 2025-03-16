import os
import requests
import matplotlib.pyplot as plt

with open(".env") as f:
    for line in f:
        key, value = line.strip().split("=")
        os.environ[key] = value

API_KEY = os.getenv("API_KEY")  
city = "Hyderabad"

url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

# Fetching data
response = requests.get(url)
data = response.json()

# Extracting weather details
temperature = data["main"]["temp"]
humidity = data["main"]["humidity"]
pressure = data["main"]["pressure"]
weather = data["weather"][0]["description"]

# Printing data
print(f"Weather in {city}: {weather}")
print(f"Temperature: {temperature}°C")
print(f"Humidity: {humidity}%")
print(f"Pressure: {pressure} hPa")

# Visualizing the data
categories = ["Temperature (°C)", "Humidity (%)", "Pressure (hPa)"]
values = [temperature, humidity, pressure]

plt.figure(figsize=(6, 4))
plt.bar(categories, values, color=["orange", "blue", "green"])
plt.title(f"Weather Conditions in {city}")
plt.ylabel("Value")
plt.show()
