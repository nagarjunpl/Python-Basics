# Comprehension

# add 1 to each element in the list using a for loop
l = [1, 2, 3, 4, 5]
sum = 0
for i in l:
    sum += i
    print(sum) # sum of elements

l= [1, 2, 3, 4, 5]
dl= []
for i in l:
    dl.append(i) # add 1 to each element in the list using a list comprehension
    print(dl)


# looping through dictionary
d = {
    'a': 1, 
    'b': 2, 
    'c': 3
    }
for i in d.items():
    print(i) # print key-value pairs

for i in d.values():
    print(i) # print values

for i in d.keys():
    print(i) # print keys


# for loop with range

students = ['Arjun', 'nagarjun', "john", 'doe']
marks = [90, 80, 70, 60]

stud_marks = {}  # create an empty dictionary to store student names and their marks

for i in range(len(students)):
    stud_marks[students[i]] = marks[i] # create a dictionary with student names as keys and marks as values

print(stud_marks)  # print the dictionary