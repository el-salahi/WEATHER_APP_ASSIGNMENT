# function to display welcome message
def welcome_message(name):
    print(f"Welcome {name}! Your weather app will display the current weather data in your area!")

# function to prompt inputting city name
def get_city_name():
    city = input("Enter city to see weather results in your area: ")
    return city

# function to prompt input and validate value inputted
def input_validate():
    # try block of code, else catch any potential errors with except below, then finally msg "op complete")
    try:
        # loop infinitely until condition (correct input data type) met
        while True:
            # try block of code, else catch errors with except block below)
            try:
                # prompt user to input city via get_city_function function and store value in a variable
                user_city = get_city_name()
                # if the variable value is an alphabetic str then return value out of function and break loop 
                if user_city.isalpha():
                    print(f"{user_city} has a valid datatype")
                    return user_city
                    break
                # if the variable value is anything else - e.g. int, float, !£$% non-alpha characters - then raise error, and loop begins again, prompting inputting another city
                else:
                    raise ValueError("Invalid datatype. Please input valid city")
            except ValueError as ve:
                print(f"Error due to: {ve}")
    # catch value error
    except ValueError as ve:
        print(f"Error due to: {ve}")
    # catch any other error
    except Exception as e:
        print(f"Error due to: {e}")
    # final block of code to run
    finally:
        print("Validation operation complete")


# importing for the purpose of testing function
# ! to be deleted
import fetch_data
weather_data = fetch_data.weather_data
# !
# function to display weather_data
def display_data():
    
    print(f"Weather conditions are {condition} today\nThe temperature is {temp}, with Wind speeds of {wind_speed} and a Humidiy of {humidity}")
