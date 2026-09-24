# Reverse an Array Using XOR Swap 🔄

This Python program reverses the elements of an array by **swapping the elements from both ends** using the **XOR (`^`) operator**.

It does not use a third variable or create another array.

## 📌 Description

The program uses two pointers:

* `i` starts from the **first element** of the array.
* `j` starts from the **last element** of the array.
* The elements at positions `i` and `j` are swapped using XOR.
* `i` is moved forward.
* `j` is moved backward.
* This continues until `i` is no longer less than `j`.

As a result, the array is reversed **in-place**.

## 💻 Program

```python
a = [10, 20, 30, 40, 50, 7]

i = 0
j = len(a) - 1

while (i < j):

    a[i] ^= a[j]
    a[j] ^= a[i]
    a[i] ^= a[j]

    i += 1
    j -= 1

print(a)
```

## 🔍 Program Tracking

Let's take:

```text
a = [10, 20, 30, 40, 50, 7]
```

The array has 6 elements.

Initially:

```text
i = 0
j = len(a) - 1
j = 5
```

So:

```text
i = 0
j = 5
```

The array is:

```text
Index:  0   1   2   3   4   5
Value: 10  20  30  40  50   7
        ↑                   ↑
        i                   j
```

---

## Step 1: Swap First and Last Elements

Current values:

```text
a[i] = 10
a[j] = 7
```

XOR swap:

```text
a[i] ^= a[j]
a[j] ^= a[i]
a[i] ^= a[j]
```

After swapping:

```text
a[0] = 7
a[5] = 10
```

Array becomes:

```text
[7, 20, 30, 40, 50, 10]
```

Move the pointers:

```text
i = 1
j = 4
```

---

## Step 2: Swap Second and Second-Last Elements

Current values:

```text
a[i] = 20
a[j] = 50
```

After XOR swap:

```text
a[1] = 50
a[4] = 20
```

Array becomes:

```text
[7, 50, 30, 40, 20, 10]
```

Move the pointers:

```text
i = 2
j = 3
```

---

## Step 3: Swap Middle Elements

Current values:

```text
a[i] = 30
a[j] = 40
```

After XOR swap:

```text
a[2] = 40
a[3] = 30
```

Array becomes:

```text
[7, 50, 40, 30, 20, 10]
```

Move the pointers:

```text
i = 3
j = 2
```

Now:

```text
i < j
3 < 2 → False
```

The loop stops.

## 📊 Complete Tracking Table

| Step    | `i` | `j` | Swapped Values | Array                |
| ------- | --: | --: | -------------- | -------------------- |
| Initial |   0 |   5 | —              | `[10,20,30,40,50,7]` |
| 1       |   0 |   5 | `10 ↔ 7`       | `[7,20,30,40,50,10]` |
| 2       |   1 |   4 | `20 ↔ 50`      | `[7,50,30,40,20,10]` |
| 3       |   2 |   3 | `30 ↔ 40`      | `[7,50,40,30,20,10]` |
| End     |   3 |   2 | Stop           | `[7,50,40,30,20,10]` |

## 🎯 Final Output

```text
[7, 50, 40, 30, 20, 10]
```

Original array:

```text
[10, 20, 30, 40, 50, 7]
```

Reversed array:

```text
[7, 50, 40, 30, 20, 10]
```

## 🧠 How XOR Swap Works

The three statements:

```python
a[i] ^= a[j]
a[j] ^= a[i]
a[i] ^= a[j]
```

swap the values without using a temporary variable.

For example:

```text
A = 10
B = 7

A = A ^ B
B = B ^ A
A = A ^ B
```

After the three operations:

```text
A = 7
B = 10
```

The same technique is applied to the first/last, second/second-last, and so on.

## 📊 Simple Logic

```text
             Start
               ↓
          Create array
               ↓
        i = 0, j = last
               ↓
            i < j?
           ↙     ↘
         Yes      No
          ↓        ↓
      XOR Swap    Stop
          ↓
       i += 1
       j -= 1
          ↓
      Check again
          ↓
        Print
        array
```

## 📚 Concepts Practiced

* Python lists
* Array indexing
* `len()` function
* `while` loop
* Two-pointer technique
* Bitwise XOR operator
* XOR swapping
* In-place array reversal
* Increment and decrement operations

## ⏱️ Complexity

* **Time Complexity:** `O(n)`
* **Space Complexity:** `O(1)`

The array is reversed in-place, so no additional array is required.

## 💡 Key Idea

```text
First  ↔ Last
Second ↔ Second-Last
Third  ↔ Third-Last
       ↓
   Continue until
   the pointers meet
```

The main idea is **two-pointer array reversal using XOR swapping without an extra variable**.
