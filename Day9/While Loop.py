# While Condition

while 2>1: 
    print("2 is greater than 1")

    break  # This will prevent an infinite loop


i=1
while i <= 10:
    print(f"This is loop {i}")
    i = i+1


is_failed = True
i=1
while is_failed :
    print(f"Attempt {i}")
    i = i+1
    if i > 10:
        break  # Stop after 10 attempts
print("I gave up after 10 attempts")

# printing even numbers from 0 to 20
is_true = True
i = 1
while is_true:
    if i % 2 != 0: # Check if the number is odd
        i = i+1
        continue  # Skip odd numbers
    print(f"This is an even number: {i}")
    i = i + 1
    if i > 20:
        break
