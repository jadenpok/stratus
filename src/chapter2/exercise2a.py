"""
Let's practice working with strings!

Strings are text wrapped in quotes. You can think of them like messages or labels.
You can combine strings together and create weather reports and messages.

The examples below show different ways to work with strings.
"""

# Create a variable called weather_condition and assign it a value of either "sunny" or "rainy"
weather_condition="rainy"
# Create another variable called city and assign it your city.
city="hosuton"
# Using the variables you just created, print a message that says: "In Houston, it is rainy".
# Instead of "Houston" and "rainy", it should say whatever values you set your variables to.
location=city + "," + weather_condition

# Now try making a third variable called temperature and assign it a value like "75 degrees".
temperature="56"
# Now use all 3 variables to print a custom message about the temperature and weather in your city.
location=city + " is," + weather_condition + " with temperatures of," + str(temperature)
print(location)
