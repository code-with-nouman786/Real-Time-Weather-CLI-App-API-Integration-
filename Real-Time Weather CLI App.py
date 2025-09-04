import requests

# Your OpenWeather API key
API_KEY = "3c3e2732df4e0aa5c46a36398c67a7db"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        "q": city + ",PK",   # city in Pakistan
        "appid": API_KEY,
        "units": "metric"    # Celsius
    }
    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"].title()
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        wind = data["wind"]["speed"]

        # Check rain data 
        rain = data.get("rain", {}).get("1h", 0)  # mm in last 1 hour
        if rain > 0:
            rain_info = f"{rain} mm (last 1h)"
        else:
            rain_info = "No rain expected"

        print(f"\n🌍 Weather in {city}:")
        print(f"   🌡️\tTemperature : {temp}°C (feels like {feels_like}°C)")
        print(f"   ☁️\tCondition   : {desc}")
        print(f"   💧  Humidity    : {humidity}%")
        print(f"   🌬️\tWind Speed  : {wind} m/s")
        print(f"   🌧️\tRain        : {rain_info}")
    else:
        print(f"\nCould not fetch weather for {city}. (Error {response.status_code})")
        try:
            print("Details:", response.json()["message"])
        except:
            pass

def main():
    print("---Pakistan Weather CLI App ---")
    city = input("🌤️  Weather in your city: ").strip()
    get_weather(city)

if __name__ == "__main__":
    main()
