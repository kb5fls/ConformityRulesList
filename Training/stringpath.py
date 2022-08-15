import sys
import os

user_input = input("Enter in the path of your file : ")


assert os.path.exists(user_input), "I did not find the file at, "+str(user_input)
f = open(user_input, 'r')
print("We found your file at the path "+str(user_input))
f.close()

