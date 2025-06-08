# FOR LOOP
# Range function - it generates a sequence of numbers

for i in range(1, 10):  # Generates numbers from 1 to 9
    print( f"{i}" * i)  # Prints a half pyramid pattern

for i in range(1, 11, 2):
    print(i)  # Prints odd numbers from 1 to 10
    print("")

for i in range(10, 0, -1):
    print(i, end="")  # Prints numbers from 10 to 1 in reverse order and end with no newline
print("")

city=["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]
for i in range(len(city)):
    print(f"City {i+1}: {city[i]}")  # Prints each city with its index
    print("")


city=["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]
for i in city:
    print(i)  # Prints each city without index

name ="nagarjun"
for index, letter in enumerate(name): # Enumerate gives both index and letter
    print(letter*(index+1)) # Prints each letter multiplied by its index+1

a= [1, 2, 3, 4, 5]
for index,num in enumerate(a):
    print(f"{num} is in {index}th index ")  # Prints index and number from the list


pers_details = {"name": "Nagarjun", "age": 20, "city": "Mandya"}
print(pers_details.items()) # Prints key-value pairs of the dictionary

for key, value in pers_details.items():
    print(f"{key} : {value}")  # Prints each key-value pair in the dictionary

# Nested for loop to print multiplication table
for i in range(1,5):
    for j in range(1,11):
        print(f"{i} * {j} = {i*j}")
    print()  # Adds a newline after each table
# Prints multiplication table for numbers 1 to 4