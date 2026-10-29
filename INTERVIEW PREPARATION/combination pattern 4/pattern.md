# Centered Pyramid Star Pattern ⭐

## 📌 Description

This Python program generates a **centered pyramid pattern** using nested `for` loops.

The pattern has two parts:

1. **Spaces** are printed before the stars to move the stars toward the center.
2. **Stars** are printed in odd numbers: `1, 3, 5, 7, ...`

For example, when `n = 5`:

```text
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
```

The number of stars in each row follows:

```text
1, 3, 5, 7, 9
```

---

# 💻 Program

```python
n = int(input("Enter a number to generate pattern : "))

for i in range(1, n + 1):

    for j in range(1, n - i + 1, 1):
        print(" ", end=" ")

    for j in range(1, i + i - 1 + 1, 1):
        print("*", end=" ")

    print()
```

---

# 🧠 Logic of the Program

The program uses:

- One **outer loop** for rows.
- One inner loop for **spaces**.
- One inner loop for **stars**.

The main logic is:

```text
Decreasing spaces + Increasing odd number of stars
```

---

# 1️⃣ Outer Loop — Controls Rows

```python
for i in range(1, n + 1):
```

If:

```text
n = 5
```

then:

```text
i = 1, 2, 3, 4, 5
```

Therefore, the program creates **5 rows**.

---

# 2️⃣ First Inner Loop — Prints Spaces

```python
for j in range(1, n - i + 1, 1):
    print(" ", end=" ")
```

The number of space iterations is:

```text
n - i
```

As `i` increases, the number of spaces decreases.

For `n = 5`:

```text
Row 1 → 4 spaces
Row 2 → 3 spaces
Row 3 → 2 spaces
Row 4 → 1 space
Row 5 → 0 spaces
```

This makes the stars move toward the left as the pyramid grows.

---

# 3️⃣ Second Inner Loop — Prints Stars

The important expression is:

```python
i + i - 1 + 1
```

Simplifying:

```text
i + i - 1 + 1
= i + i
= 2i
```

Therefore:

```python
range(1, 2*i, 1)
```

is effectively used.

The number of loop iterations is:

```text
2i - 1
```

So the number of stars is:

```text
1, 3, 5, 7, 9, ...
```

---

# 🔍 Why `i + i - 1 + 1`?

The expression:

```python
i + i - 1 + 1
```

can be simplified to:

```text
2i
```

Since Python's `range()` excludes the ending value, the number of values generated is:

```text
2i - 1
```

For example, when:

```text
i = 3
```

the expression becomes:

```text
3 + 3 - 1 + 1
= 6
```

So:

```python
range(1, 6)
```

generates:

```text
1, 2, 3, 4, 5
```

That's **5 iterations**, so 5 stars are printed.

---

# 🔍 Example

Suppose the user enters:

```text
Enter a number to generate pattern : 5
```

Therefore:

```text
n = 5
```

The outer loop runs:

```text
i = 1, 2, 3, 4, 5
```

---

# 📊 Complete Tracing

## Row 1 — `i = 1`

### Space Loop

```text
n - i
= 5 - 1
= 4
```

So, 4 space iterations.

### Star Loop

```text
i + i - 1 + 1
= 1 + 1 - 1 + 1
= 2
```

Therefore:

```python
range(1, 2)
```

prints **1 star**.

Row:

```text
        *
```

---

## Row 2 — `i = 2`

### Space Loop

```text
5 - 2 = 3
```

So, 3 space iterations.

### Star Loop

```text
2 + 2 - 1 + 1
= 4
```

Therefore:

```python
range(1, 4)
```

prints **3 stars**.

Row:

```text
      * * *
```

---

## Row 3 — `i = 3`

### Space Loop

```text
5 - 3 = 2
```

So, 2 space iterations.

### Star Loop

```text
3 + 3 - 1 + 1
= 6
```

Therefore:

```python
range(1, 6)
```

prints **5 stars**.

Row:

```text
    * * * * *
```

---

## Row 4 — `i = 4`

### Space Loop

```text
5 - 4 = 1
```

So, 1 space iteration.

### Star Loop

```text
4 + 4 - 1 + 1
= 8
```

Therefore:

```python
range(1, 8)
```

prints **7 stars**.

Row:

```text
  * * * * * * *
```

---

## Row 5 — `i = 5`

### Space Loop

```text
5 - 5 = 0
```

No spaces are printed.

### Star Loop

```text
5 + 5 - 1 + 1
= 10
```

Therefore:

```python
range(1, 10)
```

prints **9 stars**.

Row:

```text
* * * * * * * * *
```

---

# 📋 Complete Trace Table

| Row `i` | Spaces `n-i` | Star Range | Number of Stars | Pattern |
|---:|---:|---|---:|---|
| 1 | 4 | `range(1,2)` | 1 | `*` |
| 2 | 3 | `range(1,4)` | 3 | `* * *` |
| 3 | 2 | `range(1,6)` | 5 | `* * * * *` |
| 4 | 1 | `range(1,8)` | 7 | `* * * * * * *` |
| 5 | 0 | `range(1,10)` | 9 | `* * * * * * * * *` |

---

# 🔄 Pattern Logic

The pattern follows two sequences:

### Spaces

```text
4 → 3 → 2 → 1 → 0
```

Formula:

```text
n - i
```

### Stars

```text
1 → 3 → 5 → 7 → 9
```

Formula:

```text
2i - 1
```

Therefore:

```text
Spaces decrease
       ↓
Stars increase by 2
       ↓
Centered pyramid
```

---

# 🖨️ Output

For:

```text
n = 5
```

Output:

```text
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
```

---

# 🔄 Program Flow

```text
              Input n
                 ↓
          Start outer loop
                 ↓
            i = 1 to n
                 ↓
        Print n-i spaces
                 ↓
        Print 2i-1 stars
                 ↓
             New line
                 ↓
          Next value of i
                 ↓
          Repeat until n
                 ↓
               Stop
```

---

# 📚 Concepts Practiced

- Nested `for` loops
- Pattern programming
- `range()`
- Loop variables
- Arithmetic expressions
- Increasing odd-number sequence
- Decreasing spaces
- Centered pattern
- `print()` with `end`

## 💡 Key Takeaway

The two important formulas are:

```text
Number of spaces = n - i
```

and:

```text
Number of stars = 2i - 1
```

The program combines them to create a centered pyramid.

### In One Line

> **For every row, print `n-i` spaces followed by `2i-1` stars to create a centered pyramid pattern.**