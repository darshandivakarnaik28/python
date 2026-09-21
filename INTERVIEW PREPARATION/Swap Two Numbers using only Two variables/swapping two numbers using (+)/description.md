# Swap Two Numbers Using Two Variables 🔄

This Python program swaps the values of two numbers **without using a third variable**.

## 📌 Description

The program starts with two variables:

```text
a = 10
b = 5
```

It first displays the values **before swapping**.

Then, the values are swapped using only the two existing variables by performing arithmetic operations:

```text
b = a + b
a = b - a
b = b - a
```

After these operations, the values of `a` and `b` are exchanged.

## 🔍 Program Tracking

Initial values:

```text
a = 10
b = 5
```

### Step 1

```text
b = a + b
b = 10 + 5
b = 15
```

Now:

```text
a = 10
b = 15
```

### Step 2

```text
a = b - a
a = 15 - 10
a = 5
```

Now:

```text
a = 5
b = 15
```

### Step 3

```text
b = b - a
b = 15 - 5
b = 10
```

Final values:

```text
a = 5
b = 10
```

The values have been successfully swapped.

## 💡 Key Concept

The important point is that **no third variable is used**.

```text
Before Swap:
a = 10
b = 5

       ↓
   Arithmetic
   Operations
       ↓

After Swap:
a = 5
b = 10
```

## 📚 Concepts Practiced

* Python variables
* Arithmetic operators
* Assignment operator
* Swapping values
* Using only two variables
* `print()` function

## ⏱️ Complexity

* **Time Complexity:** `O(1)`
* **Space Complexity:** `O(1)`
