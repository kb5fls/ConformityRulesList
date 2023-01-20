import sys
from Calculation_Program import *
"""
Author: Phil Salem
Status: Program in progress

Purpose:
This program allows a user to perform different mathematical tasks.
Task lists:
    - Basic math functions
    - Converting temperatures between Celsius and Fahrenheit
    - Convert between metric system and Imperial System
    - Calculate Weight
    - Calculate Length
    - Calculate Area
    - Calculate Volume
    - Calculate Speed
    - Calculate Time
    - Calculate Angle
    - Calculate Pressure

Need to create function that allows user to select which
mathematical function to use which will allow user to input
in the correct type of numbers to input.

"""


mathMenu()

choice = int(input("Enter in your selection -: "))

if choice == 5:
    sys.exit("Thank You")
x = int(input("Please input your first number -: "))
y = int(input("Please input your second number -: "))

if choice == 1:
    addNum(x, y)
elif choice == 2:
    subNum(x, y)
elif choice == 3:
    mulNum(x, y)
elif choice == 4:
    divNum(x, y)
