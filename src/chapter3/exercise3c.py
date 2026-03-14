"""
Now let's learn about functions that return values!

So far, our functions have printed results. But what if you want to use the result
in other calculations? That's where return values come in.

The example below shows how to return values from functions.
"""


def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius


# Call the function and store the result
temp_celsius = convert_to_celsius(75)
print("75°F equals", temp_celsius, "°C")

"""
Notice how 'return' gives us back a value that we can store in a variable?
This is different from print - return lets us use the result later!

Now let's practice creating functions that return values!
"""

# Create a function called 'calculate_average' that takes two temperatures and returns their average
def calculate_average(temp1, temp2):
    average = ((temp1+temp2)/2)
    return average
# Call your function with temperatures 75 and 85, store the result, and print it

average_temp = calculate_average(90,12)
print(average_temp)
# Create a function called 'convert_to_fahrenheit' that takes celsius and returns fahrenheit
# Formula: (celsius * 9/5) + 32

# Test your function by converting 25°C to Fahrenheit and printing the result
