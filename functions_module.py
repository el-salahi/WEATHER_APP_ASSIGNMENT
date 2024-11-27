import re

#importing data os it can be used in functions
import fetch_data
weather_data = fetch_data.weather_data


# FUCTION: DISPLAY WELCOME MSG
def welcome_message(name):
    print(f"Welcome {name}! Your weather app will display the current weather forecast in your area!")

# FUCTION: PROMPT INPUT > USER CITY?
def get_city_name():
    city = input("Enter city to see the weather forecast in your area: ")
    # return data to be used in global scope
    return city

# FUNCTION: PROMPT INPUT (get_city_name()) AND VALIDATE VALUE
def input_validation():
    # try block of code, else catch any potential errors with except below, then finally msg "op complete")
    try:
        # loop infinitely until condition (correct input data type) met
        while True:
            # try block of code, else catch errors with except block below)
            try:
                # prompt user to input city via get_city_function function and store value in a variable
                user_city = get_city_name()

                # variable regex any characters EXECPT alphabetic (lower and upper) or white space
                regex = r"[^a-zA-Z/\s/]"
                # search and return match obj if any regex found in inputted user city - boolean true. If it only has alpha or \s then boolean false
                match = bool(re.search(regex,  user_city))

                # if match true - nonvalid char found
                if match:
                    raise ValueError("Invalid datatype. Please input valid city")
                
                # if match false - valid char (alpha or \s)
                else:
                    print("Input has valid datatype")

                    # if valid input data then return it to be used in global scope 
                    return user_city
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



# FUNCTION: DISPLAY WEATHER _DATA IF IN DICTIONARY
def display_data(city):
    # iterate through weather data key value pairs
    for key, value in weather_data.items():

        #if key matches inputted city then give weather conditions
        if key.lower() == city.lower():

            print(f"Weather forecast incoming for {key}...\nConditions are {value["conditions"]} in {key} today:\n{value["temperature"]} with a wind speed of {value["wind_speed"]} and humidity of {value["humidity"]}\n...")

            # return to stop iteration process and leave function
            return 
        
    # if full iteration occurs with no condition met, then display     
    print(f"...\nSorry, unable to display results for {city}")


# FUNCTION: PROMPT INPUT > CARRY ON/END?
def again_or_final(name):
    # loop infinite until break
    while True:
        yes_no = input("Would you like to see the weather forecast for a different city? Yes/No: ")

        # if input 'yes/Yes/YES/Y/y' then go through functions to input another city > validate > display data, then to top of loop to ask again or final 
        if yes_no.lower() == "yes":
            valid_user_city = input_validation()   
            display_data(valid_user_city.lower())

        # if anything other than 'yes/Yes/YES' then finish with message and break loop
        else:
            print(f"Thankyou for using the weather forecast app {name}. See you again next time!")
            break




