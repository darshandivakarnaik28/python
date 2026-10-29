# Right-Aligned Star Pattern ⭐

## 📌 Description

This Python program generates a **right-aligned triangular star pattern**.

The program uses two inner loops:

1. The first loop prints **spaces** to move the stars toward the right.
2. The second loop prints **stars**, increasing by one in each row.

For example, if `n = 5`:

```text
        *
      * *
    * * *
  * * * *
* * * * *
```

The number of spaces decreases while the number of stars increases.

---

# 💻 Program

```python
n = int(input("Enter the number to generate pattern : "))

for i in range(1, n + 1):

    for j in range(1, n - i + 1):
        print(" ", end=" ")

    for j in range(1, i + 1):
        print("*", end=" ")

    print()
```

---

# 🧠 Logic of the Program

The program uses an **outer loop** and **two inner loops**.

### 1. Outer Loop — Controls Rows

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

Therefore, the pattern contains **5 rows**.

---

## 2. First Inner Loop — Prints Spaces

```python
for j in range(1, n - i + 1):
    print(" ", end=" ")
```

This loop prints spaces before the stars.

The number of spaces is:

```text
n - i
```

So when the row number increases, the spaces decrease.

For `n = 5`:

```text
Row 1 → 4 spaces
Row 2 → 3 spaces
Row 3 → 2 spaces
Row 4 → 1 space
Row 5 → 0 spaces
```

This shifts the stars toward the left as the row increases.

---

## 3. Second Inner Loop — Prints Stars

```python
for j in range(1, i + 1):
    print("*", end=" ")
```

The number of stars is equal to the row number.

```text
Row 1 → 1 star
Row 2 → 2 stars
Row 3 → 3 stars
Row 4 → 4 stars
Row 5 → 5 stars
```

Therefore, the stars increase in every row.

---

# 🔍 Example

Suppose the user enters:

```text
Enter the number to generate pattern : 5
```

Therefore:

```text
n = 5
```

The outer loop runs from:

```text
i = 1 to 5
```

---

# 📊 Complete Tracing

## Row 1 — `i = 1`

### Space loop

```text
n - i = 5 - 1 = 4
```

Prints 4 spaces.

### Star loop

```text
i = 1
```

Prints 1 star.

Row:

```text
        *
```

---

## Row 2 — `i = 2`

### Space loop

```text
n - i = 5 - 2 = 3
```

Prints 3 spaces.

### Star loop

```text
i = 2
```

Prints 2 stars.

Row:

```text
      * *
```

---

## Row 3 — `i = 3`

### Space loop

```text
n - i = 5 - 3 = 2
```

Prints 2 spaces.

### Star loop

```text
i = 3
```

Prints 3 stars.

Row:

```text
    * * *
```

---

## Row 4 — `i = 4`

### Space loop

```text
n - i = 5 - 4 = 1
```

Prints 1 space.

### Star loop

```text
i = 4
```

Prints 4 stars.

Row:

```text
  * * * *
```

---

## Row 5 — `i = 5`

### Space loop

```text
n - i = 5 - 5 = 0
```

No spaces are printed.

### Star loop

```text
i = 5
```

Prints 5 stars.

Row:

```text
* * * * *
```

---

# 📋 Trace Table

| Row `i` | Spaces `n-i` | Stars `i` | Pattern |
|---:|---:|---:|---|
| 1 | 4 | 1 | `        *` |
| 2 | 3 | 2 | `      * *` |
| 3 | 2 | 3 | `    * * *` |
| 4 | 1 | 4 | `  * * * *` |
| 5 | 0 | 5 | `* * * * *` |

---

# 🔄 Pattern Logic

The main idea is:

```text
Spaces decrease
        ↓
Stars increase
```

For `n = 5`:

```text
Spaces     Stars

  4    +     1
  3    +     2
  2    +     3
  1    +     4
  0    +     5
```

Therefore:

```text
Number of spaces = n - i
Number of stars  = i
```

---

# 🖨️ Output

For input:

```text
Enter the number to generate pattern : 5
```

Output:

```text
        *
      * *
    * * *
  * * * *
* * * * *
```

> **Note:** In the actual terminal, the exact visual width of the spaces depends on the fact that `print(" ", end=" ")` prints a space and then another space through `end=" "`. The important logic is that the number of leading space iterations decreases from `n-1` to `0`.

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
          Print i stars
                 ↓
             New line
                 ↓
           Next row
                 ↓
          Repeat until i=n
                 ↓
               Stop
```

---

# 📚 Concepts Practiced

- Nested `for` loops
- Pattern programming
- `range()`
- Increasing pattern
- Decreasing pattern
- Leading spaces
- `print()` with `end`
- Loop variables

## 💡 Key Takeaway

The two important formulas are:

```python
n - i
```

→ controls the **spaces**.

```python
i
```

→ controls the **stars**.

So the pattern is created by combining:

```text
Decreasing spaces + Increasing stars
```

### In One Line

> **For every row, print `n-i` spaces first and then print `i` stars.**