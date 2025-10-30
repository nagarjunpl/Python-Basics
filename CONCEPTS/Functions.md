
# 🐍 Functions in Python

A **function** in Python is a block of reusable code that performs a specific task.  
Instead of writing the same code again and again, you can **define** a function once and **call** it whenever needed.

---

## 🧠 Basic Structure of a Function

```python
def function_name(parameters):
    # code block
    return result
```

- **`def`** → keyword used to define a function  
- **`function_name`** → the name you give to the function  
- **`parameters`** → input values (optional)  
- **`return`** → sends back a value (optional)

---

## 💡 Example 1 — Simple Function

```python
def greet():
    print("Hello, welcome to Python!")
    
greet()
```

**Output:**
```
Hello, welcome to Python!
```

---

## 💡 Example 2 — Function with Parameters

```python
def add(a, b):
    return a + b

result = add(5, 3)
print(result)
```

**Output:**
```
8
```

---

## 💡 Example 3 — Function with Default Parameter

```python
def greet(name="Guest"):
    print("Hello", name)

greet("Nagarjun")
greet()
```

**Output:**
```
Hello Nagarjun
Hello Guest
```

---

## ⚙️ Why Use Functions?

✅ **Reusability** – Write once, use many times  
✅ **Readability** – Makes code clean and organized  
✅ **Debugging** – Easier to test and fix small parts of code  
✅ **Collaboration** – Teams can divide code into separate functions  

---

## 🧩 Types of Functions in Python

| Type | Description |
|------|--------------|
| **Built-in Functions** | Already provided by Python (like `len()`, `print()`, `max()`) |
| **User-defined Functions** | Functions created by you using `def` |
| **Lambda Functions** | Small anonymous functions defined with `lambda` keyword |

### Example of Lambda Function

```python
square = lambda x: x * x
print(square(4))
```

**Output:**
```
16
```

---
