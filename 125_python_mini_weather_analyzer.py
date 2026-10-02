# 125_python_mini_weather_analyzer.py
# Mini Weather Analyzer - 10 practical features (sample data only)

weather = {
    "Monday": {"temperature": 29, "condition": "Sunny"},
    "Tuesday": {"temperature": 31, "condition": "Sunny"},
    "Wednesday": {"temperature": 27, "condition": "Cloudy"},
    "Thursday": {"temperature": 25, "condition": "Rainy"},
    "Friday": {"temperature": 30, "condition": "Sunny"},
}

print("1. Weekly weather:", weather)
print("2. Days recorded:", len(weather))
temps = [d["temperature"] for d in weather.values()]
print("3. Average temperature:", round(sum(temps) / len(temps), 2))
hottest = max(weather, key=lambda d: weather[d]["temperature"])
print("4. Hottest day:", hottest, weather[hottest]["temperature"])
coldest = min(weather, key=lambda d: weather[d]["temperature"])
print("5. Coldest day:", coldest, weather[coldest]["temperature"])
print("6. Sunny days:", [d for d, x in weather.items() if x["condition"] == "Sunny"])
print("7. Above 28 C:", [d for d, x in weather.items() if x["temperature"] > 28])
print("8. Sorted temperatures:", sorted(((d, x["temperature"]) for d, x in weather.items()), key=lambda x: x[1]))
weather["Saturday"] = {"temperature": 28, "condition": "Cloudy"}
print("9. Added Saturday:", weather["Saturday"])
conditions = {}
for info in weather.values():
    conditions[info["condition"]] = conditions.get(info["condition"], 0) + 1
print("10. Condition summary:", conditions)
