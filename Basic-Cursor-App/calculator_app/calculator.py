import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

def log10(x):
    if x <= 0:
        return "Error! Logarithm of non-positive number."
    else:
        return math.log10(x)

def ln(x):
    if x <= 0:
        return "Error! Logarithm of non-positive number."
    else:
        return math.log(x)
