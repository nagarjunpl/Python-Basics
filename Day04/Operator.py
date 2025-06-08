
# Common Assignment Operator

a = 100

a += 200 # 300 
a -= 100 # 200
a *= 2 # 400
a /= 2 # 200
a %= 2 # 0 

# Comparison Operator

a = 100
b = 200

print(a == b) # False
print(a != b) # True
print(a > b) # False
print(a < b) # True
print(a >= b) # False
print(a <= b) # True

# Logical Operator

a = 100
b = 200

print(a and b) # 200
print(a or b) # 100
print(not a) # False
print( 2>1 and 3<4) # True
print( 2>1 and 3>4) # False
print( 2>1 or 3>4) # True
print( 2<1 or 3>4) # False
print(not 2>1) # False
print(not 2<1) # True

# Membership Operator

a = [1, 2, 3, 4, 5]

print(1 in a) # True
print(6 in a) # False
print(1 not in a) # False
print(6 not in a) # True

b = "Hello"

print("H" in b) # True
print("h" in b) # False
print("H" not in b) # False
print("h" not in b) # True
