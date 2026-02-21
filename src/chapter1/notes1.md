# Chapter 1: Variables

## What are Variables?

A Variable is a container for a value. A variable consists of 2 parts: a name and a value.
For example, we might have a variable called `name` that holds the value `Bob`.

We'll need to talk about two things: 1, creating a variable, and 2, getting a variable's value.

## Creating a variable

To create a variable, you use the equals sign (`=`) to assign a value to a variable name.
Note that in code, this equal sign means "gets" rather than "equals". So `name = "Bob"` means "name gets the value Bob".

```
name = "Bob"
```

By the way, you'll notice we are continuing to make use of the quotation marks like in Chapter 0.
Words/sentences wrapped inside quotes are called Strings. We'll discuss what exactly Strings are in Chapter 2. For now, just remember to use quotes when working with text!

## Using Variables

Once you create a variable, you can later get its value by using its name.

```
name = "Bob"
print(name)
```

## Some notes about variable names

There are some conventions with variables in Python. We'll practice using these conventions:
- Descriptive (use `student_name` instead of `x`)
- Start with a letter (usually)
- Use lowercase with underscores for multiple words (e.g., `favorite_color`)
- Cannot have spaces, Python will raise an error

Good examples: `name`, `favorite_color`, `number_of_pets`

