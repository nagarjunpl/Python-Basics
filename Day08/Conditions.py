# if-else statements

# simple if statement
a=10
if a > 1:
    print("a is greater than 10") 


# if-else statement
b=20
if b % 2 == 0: # Check if b is even
    print("b is even")
else:
    print("b is odd")


# if-elif-else statement

c = 15
if c <20:
    print(f"{c} is less than 20")
elif c == 20:
    print(f"{c} is equal to 20")
else:
    print("c is greater than 20")


# input from user

d = int(input("Enter a number: "))
if d < 0:
    print("d is negative")  
elif d == 0:
    print("d is zero")
else:
    print("d is positive")

