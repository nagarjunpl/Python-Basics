# Lists

items = ["banana", "apple", "orange", "mango"]

print(items) # print all items

print(items[0]) # print first item

print(items[::-1]) # print reverse

items[0] = "pineapple" # change first item

print(items)

# Modifying Lists

items.append("kiwi") # add item
items.insert(0, "pineapple") # insert item at index 0
items.remove("apple") # remove item
items.pop() # remove last item
items.pop(0) # remove first item
items.clear() # remove all items
items.sort() # sort items
items.reverse() # reverse items

# Slicing Lists

list = [1, 2, 5, 6, 7, 3, 4, 4, 1, 10]
print(list[0:4]) # print first 4 items
print(list[0:8:2]) # print first 8 items with step 2
print(list[::2]) # print all items with step 2

# List Methods

print(sorted(list)) # sort items
print(len(list)) # print length of list
print(list.count(1)) # count number of 1s in list
print(sum(list)) # sum of all items in list


# adding strings, numbers, booleans, lists, tuples, dictionaries, sets, and other lists to the list

list1 = ["bat", 20, True, 20.5, [1, 2, 3], (1, 2, 3), {1, 2, 3}, {1: "one", 2: "two", 3: "three"}]

print(list1[4]) # list
print(list1[4][1]) # list
print(list1[5][1]) # tuple
print(list1[6]) # set
print(list1[7]) # dictionary

s1.extend(s2) # combine two lists
print(s1)
