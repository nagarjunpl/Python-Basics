# Accessing Characters in a String

course = "Python"

print(course)

print(course[0]) # first character

print(course[-1]) # last character

print(course[0:3]) # first 3 characters

print(course[1:5]) # from index 1 to 4

print(course[1:]) # from index 1 to end

print(course[:3]) # from start to index 2

print(course[1:5:2]) # from index 1 to 4 with step 2

print(course[::2]) # from start to end with step 2

print(course[::-1]) # reverse the string

# escape sequences

message = "i'm a \"nagarjun\"" # using double quotes inside single quotes
message = "i'm a \n nagarjun" # new line
message = "i'm a \t nagarjun" # tab
message = "i'm a \\ nagarjun" # backslash
message = "i'm a \r nagarjun" # carriage return
message = "i'm a \f nagarjun" # form feed
message = "i'm a \b nagarjun" # backspace
message = "i'm a \a nagarjun" # alert

print(message)


