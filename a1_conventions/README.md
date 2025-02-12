# Conventions in Python

Python has an official style guide called [python enhancement proposal 8 (PEP8)](https://peps.python.org/pep-0008/#introduction), which contains a comprehensive style guide improve readability and consistency. This is a good reference material, to check up things from times to times. In this document we'll cover some basic conventions that you should follow in your code to make it easier for other python programmers to follow. 

## Variable and function names

Use `snake_case`, which means lowercase for all letters and underscores '_' to separate words. 

## Class names

Use PascalCase, which means uppercase for first character for each new word. 

## Clear readable naming 

The names of your variables, functions, classes should be readable rather than short and abbreviated. For example 

```py
def calculate_discount(price, discount_rate):
    return price * (1 - discount_rate)
```

and not 

```py
def disc(p, d):
    return p * (1 - d)
```

> [!NOTE]
> short variables can be used as iteration variable for example 
> ```py
> for i in range(5):
>     print(i)

## Type hints

As Python is dynamically typing, it is good to use type hints for function parameters and return values so that other developers can see which types are intended

```py
def add_numbers(number1: int, number2: int) -> int:
    return number1 + number2
```

## Iteration variable

Iteration variable can be short in this example: 

```py
for i in range(5):
    print(i)
```

When looping through a list/tuple, use a descriptive variable, for example 

```py
fruits = ["apple", "orange", "grape"]
for fruit in fruits:
    print(fruit)
```

## Underscore iteration variable

When you don't use the iteration variable, you use underscore to denote it 

```py
for _ in range(5):
    print("hello")
```

## Private by convention

In python, there are no private variables such as in many other languages. Instead you use underscore before the function name or the method name to indicate private

```py
def _private_function():
    ...
```

> ![NOTE]
> you can still access this function but shouldn't if you are outside of the class/module. 
