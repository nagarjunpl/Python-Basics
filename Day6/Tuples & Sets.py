# Tuples
# Tuples are immutable, meaning they cannot be changed once created

gender = ('male', 'female', 'non-binary')

print(gender[0]) # access the first element

print(gender.count("female")) # count the number of times a value appears in the tuple

print(gender[0:2])

number = (1, 2, 3, 4, 5, (1, 2, 3)) *3 # repeat the tuple 3 times

print(len(number)) # length of the tuple
print(number) #
print(number[5][2]) # access the 6th element




