"""
Now let's learn about using conditionals INSIDE functions!
"""


# Here's an example function that uses if/else to make decisions
def check_temperature(temp):
    if temp > 80:
        print("It's hot outside!")
    else:
        print("It's not too hot today!")


# Call the function to test it
check_temperature(85)
check_temperature(70)

"""
Notice how the conditional logic is inside the function?
This makes our code reusable - we can check any temperature by calling the function!
"""

# Example 1: Create a function that checks weather conditions
# Create a function called 'weather_advice' that takes a parameter called 'condition'
# - If condition equals "rainy": print "Bring an umbrella!"
# - Else: print "Enjoy the weather!"
def weather_advice(condition):
    if condition=="rainy":
        print("Bring an umbrella!")
    else:
        print("Enjoy the weather!")

# Test your function by calling it with different weather conditions like "rainy" and "sunny"
weather_advice("rainy")
weather_advice("sunny")
# Example 2: Create a function that gives clothing advice
# Create a function called 'clothing_advice' that takes a parameter called 'temperature'
# - If temperature is greater than 75: print "Wear light clothes!"
# - Else: print "You might need a jacket!"
def clothing_advice(temperature):
    if temperature > 75:
        print("wear light clothes")
    else:
        print("you might need a jacket")
# Test your function by calling it with different temperatures like 80 and 65
clothing_advice(65)
clothing_advice(80)
