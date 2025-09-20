
# Tuples in Python

## ✅ What is a Tuple?
- A **tuple** is a collection of items in Python, just like a list.  
- But the key difference is: **tuples are immutable**, meaning once created, their elements **cannot be changed, added, or removed**.  
- Tuples are written with **parentheses `()`**.

---

## 📝 Example
```python
# Creating a tuple
numbers = (1, 2, 3, 4, 5)
print(numbers)

# Accessing elements
print(numbers[0])   # first element → 1
print(numbers[-1])  # last element → 5

# Tuples can store different data types
info = ("Nagarjun", 21, True, 78.5)
print(info)
```

---

## ⚡ Key Points
- **Immutable** → can’t change elements.
- **Ordered** → items have a fixed order.
- **Allows duplicates** → `(1, 2, 2, 3)` is valid.
- Can contain **different data types**.
