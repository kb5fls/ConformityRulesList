"""
Author: Phil Salem
Purpose:
    This program defines various mathematical functions to be called from the math.py program.
    The functions range from basic math functions to physics calculations
"""


def mathMenu():
    print("Select which math function you want to perform")
    print("1 - Add two numbers")
    print("2 - Subtract two numbers")
    print("3 - Multiple two numbers")
    print("4 - Divide two numbers")


def addNum(x, y):
    print("Sum is -: ", x + y)


def subNum(x, y):
    print("Difference is -: ", x + y)


def mulNum(x, y):
    print("Product is -: ", x + y)


def divNum(x, y):
    print("Division is -:", x / y)


# Functions to convert temperatures between Celsius and Fahrenheit

# Functions to calculate Length

# Functions to calculate Area

# Functions to calculate Volume

# Functions to calculate Speed
def avgSpeed(d, t):
    print("The average speed is -: ", d / t)


# Functions to calculate Acceleration
def acceleration(v, u, t):
    a = (v - u) / t
    print("The acceleration is -: ", a)

# Functions to calculate Angle

# Functions to calculate Pressure
