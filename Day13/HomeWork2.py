# Basic dictionary operations

dishes = {
    "pasta": 1299,
    "burger": 1099,
    "salad": 899,
    "pizza": 1199,
    "soda": 199
}
print("Original dishes:", dishes)

dishes["soup"] = 499  # Add a new dish

dishes["burger"] = 1199  # Update the price of an existing dish

print("Updated dishes:", dishes)

del dishes["soda"]  # Remove a dish
print("Dishes after removal:", dishes)

print(dishes.keys())  # Print all dish names
print(dishes.values())  # Print all dish prices


# Nested dictionary example

friends = {
    "arjun": {
        "age": 20,
        "city": "Mandya"
    },
    "nagarjun": {
        "age": 10,
        "city": "Mysuru"
    },
    "Charlie": {
        "age": 28,
        "city": "Bengaluru"
    }
}
print("Friends dictionary:", friends)

print("Arjun's details:", friends["arjun"])  # Accessing nested dictionary

print(friends["nagarjun"]["age"])  # Accessing a specific value in nested dictionary

# Meal time checker

time = int(input("Enter the time : ")) # 0-23

if time == 8:
    print("It's breakfast time!")
elif time == 13:
    print("It's lunch time!")
elif time == 20:
    print("It's dinner time!")
else:
    print("It's not meal time!")

# simple eligibility checker
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
elif age == 18 :
    print("You are just eligible to vote.")
else:
    print("You are not eligible to vote.")