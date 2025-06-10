# Dictionary Comprehension

names = {'Arjun', 'Nagarjun', 'John', 'Doe'}

s = {name: len(name) for name in names}  # create a dictionary with names as keys and their lengths as values
print(s)  # print the dictionary with names and their lengths

# Dictionary comprehension with condition
cities = {'Mysuru': 20000, "Mandya":5000, 'Bangalore':50000, 'Chennai':40000, 'Delhi' :60000}
d = {key:value for key, value in cities.items() if value > 30000}  # create a new dictionary with cities having population greater than 30000
print(d)  # print the new dictionary with cities having population greater than 30000

# Split a string into a dictionary
s = 'name:Arjun, age: 25, city: Mysuru'
d = {item.split(':')[0]: item.split(':')[1].strip() for item in s.split(',')}  # create a dictionary from a string with key-value pairs 
print(d)

# List input with split
print("LIST INPUT")

l = [int(num) for num in input("Enter numbers separated by space: ").split()]  # take input from user and create a list of integers
print(l)  # print the list of integers