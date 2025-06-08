
# Dictionaries

birthdays = { "Nagarjun" : "dec 2",
               "Alice" : "April 1",
               "sarju": "june 3",
               "Bob": "May 5",
               "akash": 2000, # Mixed data types
 }

print(birthdays)
print(birthdays["Nagarjun"]) # Accessing a value using a key
print(birthdays.get("arjun","NOT FOUND")) # Using get method to avoid KeyError

birthdays["arjun"] = "May 5" # Adding a new key-value pair
print(birthdays)

birthdays["Nagarjun"] = "dec 3" # Updating an existing key-value pair
print(birthdays)

birthdays.pop("Alice") # Removing a key-value pair
print(birthdays)
         # OR
del birthdays["Bob"] # Deleting a key-value pair
print(birthdays)

print(birthdays.keys()) # Getting all keys
print(birthdays.values()) # Getting all values
print(birthdays.items()) # Getting all key-value pairs



person1 = {
    "name": "arjun",
    "age": 20,
    "village": "Peehalli",
}
person2 = {
    "name": "Nagarjun",
    "age": 21,
    "village": "Mandya",
}
person3 = {
    "name": "Sarju",
    "age": 22,
    "village": "Bangalore",
}

people = [person1, person2, person3] # List of dictionaries
print(people)