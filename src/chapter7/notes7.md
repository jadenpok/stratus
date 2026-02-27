# Chapter 7: Dictionaries

## What are Dictionaries?

A dictionary is a collection of **key-value pairs**. Think of it like a real dictionary where you look up a word (the key) to find its definition (the value). Or like a contact list where you look up a name to find a phone number.

In weather data, you might want to map cities to their temperatures:

- "Houston" → 85
- "Austin" → 82
- "Dallas" → 88

Instead of maintaining separate lists for cities and temperatures, a dictionary keeps them paired together.

## Creating Dictionaries

Dictionaries are created using curly braces `{}` with `key: value` pairs separated by commas:

```python
city_temps = {
    "Houston": 85,
    "Austin": 82,
    "Dallas": 88
}
```

You can also create an empty dictionary:

```python
weather_data = {}
```

Keys are typically strings, but values can be any type:

```python
houston_weather = {
    "temperature": 85,
    "condition": "sunny",
    "humidity": 60,
    "is_raining": False
}
```

## Accessing Dictionary Values

Use square brackets with the key to get its value:

```python
city_temps = {
    "Houston": 85,
    "Austin": 82,
    "Dallas": 88
}

print(city_temps["Houston"])  # Output: 85
print(city_temps["Austin"])   # Output: 82
```

You can also use the `.get()` method, which won't cause an error if the key doesn't exist:

```python
temp = city_temps.get("Seattle")
print(temp)  # Output: None

# Provide a default value if key doesn't exist
temp = city_temps.get("Seattle", 70)
print(temp)  # Output: 70
```

## Adding and Modifying Values

Add a new key-value pair or update an existing one using assignment:

```python
city_temps = {"Houston": 85}

# Add a new city
city_temps["Austin"] = 82
print(city_temps)  # {"Houston": 85, "Austin": 82}

# Update Houston's temperature
city_temps["Houston"] = 88
print(city_temps)  # {"Houston": 88, "Austin": 82}
```

## Removing Items

Remove items using `del` or `.pop()`:

```python
city_temps = {"Houston": 85, "Austin": 82, "Dallas": 88}

# Remove using del
del city_temps["Austin"]
print(city_temps)  # {"Houston": 85, "Dallas": 88}

# Remove using pop (returns the value)
temp = city_temps.pop("Dallas")
print(temp)        # 88
print(city_temps)  # {"Houston": 85}
```

## Dictionary Methods

### keys() - Get all keys

```python
city_temps = {"Houston": 85, "Austin": 82, "Dallas": 88}
print(city_temps.keys())  # dict_keys(['Houston', 'Austin', 'Dallas'])
```

### values() - Get all values

```python
print(city_temps.values())  # dict_values([85, 82, 88])
```

### items() - Get all key-value pairs

```python
print(city_temps.items())
# dict_items([('Houston', 85), ('Austin', 82), ('Dallas', 88)])
```

## Checking for Keys

Use `in` to check if a key exists:

```python
city_temps = {"Houston": 85, "Austin": 82}

if "Houston" in city_temps:
    print("Houston is in the dictionary!")

if "Seattle" not in city_temps:
    print("Seattle is not in the dictionary!")
```

## Iterating Through Dictionaries

Loop through keys:

```python
city_temps = {"Houston": 85, "Austin": 82, "Dallas": 88}

for city in city_temps:
    print(city)
# Houston
# Austin
# Dallas
```

Loop through values:

```python
for temp in city_temps.values():
    print(temp)
# 85
# 82
# 88
```

Loop through both keys and values:

```python
for city, temp in city_temps.items():
    print(city, "is", temp, "degrees")
# Houston is 85 degrees
# Austin is 82 degrees
# Dallas is 88 degrees
```

## Lists vs Dictionaries: When to Use Each

**Use a list when:**

- You have a simple collection of items
- Order matters
- Items are accessed by position/index
- Example: `temperatures = [75, 78, 72, 80]`

**Use a dictionary when:**

- You need to look up values by a meaningful key
- You're associating related pieces of data
- Order doesn't matter (though Python 3.7+ maintains insertion order)
- Example: `city_temps = {"Houston": 85, "Austin": 82}`

**You can combine them:**

```python
# List of dictionaries
cities_data = [
    {"name": "Houston", "temp": 85, "condition": "sunny"},
    {"name": "Austin", "temp": 82, "condition": "cloudy"}
]

# Dictionary with lists as values
city_forecasts = {
    "Houston": [85, 87, 84, 82, 80],
    "Austin": [82, 83, 81, 79, 77]
}
```

## Why Use Dictionaries?

1. **Meaningful Lookup** - Access data by meaningful keys instead of numeric indices
2. **Data Association** - Keep related data together (city and temperature)
3. **Efficient Lookup** - Fast to find a value by its key
4. **Readability** - Code is more self-documenting with named keys
5. **Flexibility** - Easy to add, remove, or update key-value pairs

Dictionaries are perfect for structured data like weather reports, user profiles, configuration settings, and any scenario where you're mapping one thing to another!
