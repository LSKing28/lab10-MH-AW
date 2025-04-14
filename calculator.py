"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math


# First example
def add(a, b): 
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    if b == 0:
        raise ZeroDivisionError
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

