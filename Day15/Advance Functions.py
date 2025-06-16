# variable lenght arguments

def add(*a):
    print(a)  # tuple of arguments
    print(type(a))  # type of the arguments
    print(sum(a))  # sum of the arguments

add(1, 2, 3, 4, 5) 


# **kwargs** allows you to pass a variable number of keyword arguments to a function.

def info(**details):
    print(details)  # dictionary of keyword arguments
    for key, value in details.items():
        print(f"{key} : {value}")

info(name="Nagarjun", age=25, city="Hyderabad")


# Lambda functions are small anonymous functions defined with the lambda keyword.

addition = lambda x, y, z: x + y + z
print(addition(10, 20, 30))  # calling the lambda function

double = lambda x: x ** 2
print(double(5))  # calling the lambda function


students = [
    {"name": "Nagarjun", "marks" : 90},
    {"name": "Arjun", "marks" : 85},
    {"name": "Dani", "marks" : 95}
]

students.sort(reverse=True, key = lambda a: a["marks"])  # sorting the list of dictionaries by marks
print(students)  # printing the sorted list of dictionaries


# Recursion

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
print(factorial(5))  # calling the recursive function to calculate factorial of 5

# Nested Functions
def outer_function():
    def inner_function():
        print("This is the inner function")
    inner_function()  # calling the inner function

outer_function()  # calling the outer function which in turn calls the inner function

# Nested Functions with Parameters
def addition(x, y):
    def inner_addition():
        print(x + y)
    def inner_subtraction():
        print(x - y)
    def inner_multiplication():
        print(x * y)
    def inner_division():
        print(x / y)
    inner_addition()  # calling the inner function to perform addition
    inner_subtraction() # calling the inner function to perform subtraction
    inner_multiplication()  # calling the inner function to perform multiplication
    inner_division()  # calling the inner function to perform division

addition(10, 5) # calling the function to perform addition
