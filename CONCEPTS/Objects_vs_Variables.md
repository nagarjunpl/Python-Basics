# Difference Between Objects and Variables in Python

## 1. Variables
- A **variable** is just a name (or label) that refers to a value in memory.  
- It does not store the value itself, but it points to the location where the value (object) is stored.

### Example:
```python
x = 10
y = "Hello"
```
Here:
- x and y are variables.

- They point to objects 10 (integer) and "Hello" (string).

## 2. Objects
- In Python, everything is an object (numbers, strings, lists, functions, even classes).
- An object is an instance of a class that holds data and methods.

### Example:
```
name = "Nagarjun"
```
Here:
- "Nagarjun" is an object of the class str.
- name is the variable that points to this string object.

# Key Differences Between Variables and Objects

| Aspect      | Variable                              | Object                                |
|-------------|---------------------------------------|----------------------------------------|
| Definition  | A name (label) that refers to data in memory | An instance of a class (data + behavior) |
| Role        | Points to an object                   | Stores data and methods                 |
| Example     | `x`, `y`, `name`                     | `10`, `"Hello"`, `[1, 2, 3]`           |


## Example
```
name = "nagarjun"
ob1 = 50
```
Explanation
- Variables:
  - name → variable
  - ob1 → variable
    (They are just names/labels pointing to values in memory.)
- Objects:
  - "nagarjun" → object of class str (string object)
  - 50 → object of class int (integer object)
✅ So here:
- Variables: name, ob1
- Objects: "nagarjun", 50
