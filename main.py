#import my modules from function_modules.py
import functions_module

#simulate fetching data from API - importing data from fetch_data.py
import fetch_data

import re

# assigning to variable weather_data
weather_data = fetch_data.weather_data

# run welcome
functions_module.welcome_message("Ella")

# get user input with a valid data type
valid_user_city = functions_module.input_validation()


# check user input is in weather_data, display data
functions_module.display_data(valid_user_city)

functions_module.again_or_final("Ella")
