# Dictionaries are used to store key-value pairs

my_dict = {1: 'Python', 2: 'Java'}
print(my_dict)
my_dict[2] = 'C++' # Changing element in dictionary
print(my_dict)
my_dict[3] = 'Ruby' # Adding key-value pair
print(my_dict)

# Deleting key, value pairs
# To delete the values use the pop() function which returns the value that has been deleted
# To retrieve the key-value pair, use the popitem() function which returns a tuple of a key and value
# The popitem() method removes the item that was last inserted into the dictionary
    #  The removed item is the return value of popitem()
# To clear the entire dictionary use the clear() function
dict = {'first': 'Python', 'second': 'Java', 'third': 'C++', 'fourth': 'Ruby'}
print(dict)
a = dict.pop('third') # Removes the key-value pair and returns the value removed
print('Value:', a)
print('Dictionary:', dict)
b = dict.popitem() # pop the key-value pair
print('key, value pair', b)
print('Dictionary:', dict)

# Access elements using the keys only. You can access the elements using the get() function or pass the key value
print(dict['first'])
print(dict.get('second'))
print(dict.get('third'))

# Functions which returns keys or the values of the key-value pair accordingly to the keys(), values(), items()
cars = {'firstbrand': 'Ford',
        'firstmodel': 'Mustang',
        'firstyear': 1967,
        'secondbrand': 'Honda',
        'secondmodel': 'Pilot',
        'secondyear': 2017}
print(cars)
print("Dictionary Keys: ", cars.keys()) # Prints keys of dictionary
print("Dictionary Values: ", cars.values()) # Prints the values of the dictionary
print("Dictionary Key-Value pairs: ", cars.items()) # Prints key-value pairs
print("Dictionary first value: ", cars.get('firstbrand'))