# Swap Two Numbers Using XOR 🔄

This Python program swaps two numbers using the **XOR (`^`) operator**, without using a third variable.

## 📌 Description

The program takes two numbers `a` and `b` as input and swaps their values using three XOR operations.

The main logic is:

```text
b = a ^ b
a = a ^ b
b = b ^ a
```

The XOR operation allows the original values to be recovered and exchanged without requiring an additional variable.

## 💻 Program

```python
def get_swap(a, b):

    print("Before swap a=", a)
    print("Before swap b=", b)

    b = a ^ b
    a = a ^ b
    b = b ^ a

    print("After swap a=", a)
    print("After swap b=", b)


a = int(input("Enter a :"))
b = int(input("Enter b :"))

get_swap(a, b)
```

## 🔍 Program Tracking

Let's take:

```text
a = 10
b = 5
```

Initially:

```text
a = 10
b = 5
```

### Step 1

```text
b = a ^ b
```

Convert the numbers to binary:

```text
10 = 1010
 5 = 0101
```

Perform XOR:

```text
  1010
^ 0101
------
  1111
```

`1111` in decimal is `15`.

Therefore:

```text
a = 10
b = 15
```

---

### Step 2

```text
a = a ^ b
```

Now:

```text
a = 10
b = 15
```

Binary:

```text
10 = 1010
15 = 1111
```

XOR:

```text
  1010
^ 1111
------
  0101
```

`0101` in decimal is `5`.

Therefore:

```text
a = 5
b = 15
```

---

### Step 3

```text
b = b ^ a
```

Now:

```text
b = 15
a = 5
```

Binary:

```text
15 = 1111
 5 = 0101
```

XOR:

```text
  1111
^ 0101
------
  1010
```

`1010` in decimal is `10`.

Therefore:

```text
a = 5
b = 10
```

The values are successfully swapped.

## 📊 Tracking Table

| Step    | Operation   |  a |  b |
| ------- | ----------- | -: | -: |
| Initial | —           | 10 |  5 |
| 1       | `b = a ^ b` | 10 | 15 |
| 2       | `a = a ^ b` |  5 | 15 |
| 3       | `b = b ^ a` |  5 | 10 |

### Before Swap

```text
a = 10
b = 5
```

### After Swap

```text
a = 5
b = 10
```

## 🧠 Understanding XOR

XOR is a **bitwise operator** that compares corresponding bits.

The basic XOR rules are:

```text
0 ^ 0 = 0
0 ^ 1 = 1
1 ^ 0 = 1
1 ^ 1 = 0
```

An important property used here is:

```text
A ^ A = 0
A ^ 0 = A
```

These properties allow the values to be swapped.

## 📊 Simple Flow

```text
              Start
                ↓
           Get a and b
                ↓
       Print before swap
                ↓
          b = a ^ b
                ↓
          a = a ^ b
                ↓
          b = b ^ a
                ↓
        Print after swap
                ↓
               End
```

## 📚 Concepts Practiced

* Python functions
* Function arguments
* Bitwise XOR operator `^`
* Binary representation
* Swapping values
* Variables
* `print()` function
* User input

## ⏱️ Complexity

* **Time Complexity:** `O(1)`
* **Space Complexity:** `O(1)`

Only a fixed number of XOR operations are performed.

## 💡 Key Idea

```text
Two variables
     ↓
XOR operation
     ↓
No third variable
     ↓
Values are swapped
```

This program demonstrates how **bitwise XOR can be used to swap two integer values without an extra variable**.
