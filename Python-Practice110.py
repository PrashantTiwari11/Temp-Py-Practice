# 108_python_mini_weather_report.py
# Mini Weather Data Analyzer - 10 practical features
# Uses sample data for offline practice.

weather = [
    {"city": "Rajkot", "temp": 34, "humidity": 55},
    {"city": "Ahmedabad", "temp": 36, "humidity": 50},
    {"city": "Delhi", "temp": 32, "humidity": 60},
    {"city": "Mumbai", "temp": 30, "humidity": 75},
    {"city": "Jaipur", "temp": 35, "humidity": 45},
]

print("1. Weather data:", weather)

temperatures = [item["temp"] for item in weather]
print("2. Temperatures:", temperatures)

average = sum(temperatures) / len(temperatures)
print("3. Average temperature:", round(average, 2))

hottest = max(weather, key=lambda item: item["temp"])
print("4. Hottest city:", hottest["city"], hottest["temp"])

coldest = min(weather, key=lambda item: item["temp"])
print("5. Coldest city:", coldest["city"], coldest["temp"])

humidity = [item["humidity"] for item in weather]
print("6. Average humidity:", round(sum(humidity) / len(humidity), 2))

hot = [item["city"] for item in weather if item["temp"] >= 35]
print("7. Hot cities:", hot)

humid = [item["city"] for item in weather if item["humidity"] >= 70]
print("8. High humidity cities:", humid)

sorted_weather = sorted(weather, key=lambda item: item["temp"], reverse=True)
print("9. Sorted by temperature:", sorted_weather)

summary = {
    "cities": len(weather),
    "average_temperature": round(average, 2),
    "hottest": hottest["city"],
    "coldest": coldest["city"]
}
print("10. Weather summary:", summary)
