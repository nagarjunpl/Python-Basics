# list comprehension

l = [1,2,3,4,5,6,7]
dl = [i*2 for i in l]  # create a new list with each element multiplied by 2 using list comprehension
print(dl)  # print the new list

l = [i for i in range(1, 11)]  # create a list of numbers from 1 to 10
dl = [i**2 for i in l] # create a new list with each element squared using list comprehension
print(dl)

# List comprehension with condition
n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
s = [i**2 for i in n if i % 2 == 0]  # create a new list with only even numbers from the original list
print(s)  # print the new list with even numbers


subjects = ['math', 'science', 'english', 'history']
a = [x[1] for x in subjects] # create a new list with the second character of each subject
print(a)  # print the new list with second characters

