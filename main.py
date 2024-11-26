#import my modules from function_modules.py
import functions_module

#simulate fetching data from API - importing data from fetch_data.py
import fetch_data

# assigning to variable weather_data
weather_data = fetch_data.weather_data


# run welcome
functions_module.welcome_message("Ella")

# run get city name and assign result to a variable
# user_city = functions_module.get_city_name()
# print(user_city)


valid_user_city = functions_module.input_validate()
print(valid_user_city)
