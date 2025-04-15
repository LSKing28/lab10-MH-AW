# https://github.com/LSKing28/lab10-MH-AW
# Partner 1: Mattias Hird
# Partner 2: Andy Weisenborn

import math


# First example
def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    return b / a
def log(a, b):
    if a == 1:
        raise ValueError("Base can't equal 1")
    elif a < 0:
        raise ValueError("Base must be greater than 0")
    elif b < 0:
        raise ValueError("Argument must be greater than 0")
    return math.log(b, a)
def exp(a, b):
    return a ** b

import math

def square_root(a):
    if a < 0:
        raise ValueError("Cannot take square root of a negative number.")
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def logarithm(a, b):
    if a <= 0 or b <= 0 or a == 1:
        raise ValueError("Invalid input for logarithm.")
    return math.log(b, a)

def exponent(a, b):
    return a ** b

