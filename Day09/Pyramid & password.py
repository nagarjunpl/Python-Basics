  
# printing half pyramid using while loop

i=0
while i < 10:
    print(" + " * i)
    i += 1

# Printing half pyramid using nested while loops
a=0
while a < 10:
    b = 0
    while b <= a:
        print(" + ", end="")
        b += 1
    print()  # Move to the next line after each row
    a += 1

# Password validation using while loop
password = 1234

input_password = int(input("Enter your password: "))
if password == input_password :
    print("Access granted")
else:
    print("Access denied")

# Password validation with retry limit
attempts = 0
password1 = 1234
while attempts < 3:
    in_password = int(input("Enter your password: "))

    if password1 == in_password :
        print("Access granted")
        break
    else:
        print("Wrong password, try again")
        print("You have", 2- attempts, "attempts left")
        attempts += 1
