
boy = input("Enter boy name : ")
girl = input("Enter girl name : ")

boy_age = int(input("Enter boy age : "))
girl_age = input("Enter girl age : ") # Here take a string type

age_calculate = boy_age - int(girl_age) # convert girl age into a int 
print(boy + " loves " + girl + ". Age difference is " + str(age_calculate))


age_calculate = abs(boy_age - int(girl_age)) #abs is used for returns a positive number

print(boy + " loves " + girl + ". Age difference is " + str(age_calculate))

# another method for concatenate
print(f"{boy} loves {girl}. Age difference is {age_calculate}") # here using a formated string. It's clean, readable, and avoids the need for + and str() conversions.