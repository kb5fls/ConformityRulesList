from collections import Counter

list = []

num = int(input("Enter in the number of entries  :"))
for i in range(0,num):
    item = str(input("Enter in your number : "))
    # Add number into list
    list.append(item)

count = Counter(list)
print(count)