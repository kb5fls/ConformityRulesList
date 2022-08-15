# Tuples are the same as lists with the exception that the data once written to the tuple
# cannot be changed no matter what. The only exception is when the data inside is mutable
# only then can the tuple data be changed.
# Creation of tuples are created with parenthesis

tuple = (1, 2, 3)
print(tuple)

# Accessing values in a tuple
tuple2 = (4, 5, 6, 'Philip')
for x in tuple2:
    print(x) # Prints value from each index one at a time from the for loop
print(tuple2[0]) # Prints value from the first index
print(tuple2[:]) # Prints entire tuple
print(tuple2[3][-3:]) # Prints last 3 characters from the 4th tuple

# Appending values to a tuple use the + operator which will take another tuple to be appended to it
tuple3 = (7,8,9)
tuple3 = tuple3 + (10, 11, 12)
print(tuple3)
