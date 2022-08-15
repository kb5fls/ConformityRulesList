# Sets are a collection of unordered elements that are unique.
# Even if the data is entered more than once the data will be entered into the set only once.

set = {1, 2, 3, 4, 5, 5, 5, }
print(set)

set.add(6) # adding elements to the set using the add() function
print(set)

# Operations performed on sets
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print(set1.union(set2), '-----', set1 | set2)
print(set1.intersection(set2), '-----', set1 | set2)
print(set2.difference(set1), '-----', set1 | set2)
print(set2.difference(set1)) # Prints difference from set2 between set1 and set2
print(set1.symmetric_difference(set2)) # Prints values from both sets and not the values that are in both sets
print(set1.symmetric_difference(set2), '-----', set1 | set2)
