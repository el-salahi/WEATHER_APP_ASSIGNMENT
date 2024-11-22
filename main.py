weather_data = { "London": {"temperature": "15°C", "conditions": "Cloudy", 
"wind_speed": "5 km/h", "humidity": "80%"}, "New York": {"temperature": 
"20°C", "conditions": "Sunny", "wind_speed": "10 km/h", "humidity": 
"50%"}, "Tokyo": {"temperature": "18°C", "conditions": "Rainy", 
"wind_speed": "7 km/h", "humidity": "90%"}, "Sydney": {"temperature": 
"22°C", "conditions": "Windy", "wind_speed": "15 km/h", "humidity": 
"60%"}, "Paris": {"temperature": "17°C", "conditions": "Foggy", 
"wind_speed": "3 km/h", "humidity": "85%"} }

import functions_module

functions_module.welcome_message("Ella")

user_city = functions_module.get_city_name()
print(user_city)