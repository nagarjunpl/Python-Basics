# Sets
# Sets are unordered and unindexed, and do not allow duplicate values

set = {"apple", "banana", "cherry"}
print(set)

set.add("orange") # add an element to the set
print(set)
set.discard("cherry")
set.remove("banana") # remove an element from the set
print(set)
set.clear()
print(set)

s1 = {1, 2, 3}
s2 = {3, 4, 5, 6}

print(s1.union(s2)) # combine two sets
print(s1.intersection(s2)) # find the intersection of two sets

print(s1 | s2) # combine two sets
print(s1 & s2) # find the intersection of two sets
print(s1 - s2) # Minus of two sets

