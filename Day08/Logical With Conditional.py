# logical operators

e = 5
f = 10

# if not operator

if not (e > 10):
    print("e is not greater than 10")

# if-else with logical operators

if e < 10 and f > 5:
    print("Both conditions are true")
else:
    print("At least one condition is false")

gender = input("Enter your Gender : ")
age = int(input("Enter your Age : "))

if gender == "Female" or gender == "female:":
    print("Ticket is Free!!!")
else :
    if age > 18 and age < 60:
        print("Ticket is 20")
    elif age >= 60:
        print("Ticket is 15 (Senior Citizen)")
    elif age <= 18 and age > 12:
        print("Ticket is 10 (50% discount)")
    elif age <= 12:
        print("Ticket is Free!!!")   
