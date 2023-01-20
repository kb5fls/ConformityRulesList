def square(x):
    return x * x


input_list = [2, 3, 4, 5, 6]
# Without lambda 
result = map(square, input_list)
# Using lambda function 
result = map(lambda x: x * x, input_list)
# converting the numbers into a list
list(result)
# Output: [4, 9, 16, 25, 36]
print(list)
