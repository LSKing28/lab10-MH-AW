# https://github.com/LSKing28/lab10-MH-AW
# Partner 1: Mattias Hird
# Partner 2: Andy Weisenborn

import math

def square_root(a):
    if a < 0:
        raise ValueError("Cannot compute square root of negative number.")
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return b / a

def logarithm(a, b):
    if a <= 0 or b <= 0 or a == 1:
        raise ValueError("Invalid input for logarithm.")
    return math.log(b, a)

def exponent(a, b):
    return a ** b

