# Right-Aligned Inverted Star Triangle ⭐

## 📌 Description

This Python program generates a **right-aligned inverted triangle pattern** using nested `for` loops.

The program uses two inner loops:

1. The first loop prints **spaces** before the stars.
2. The second loop prints **stars**.

As the row number increases:

- Spaces **increase by 1**
- Stars **decrease by 1**

For example, when `n = 5`:

```text id="1x7e4d"
* * * * *
  * * * *
    * * *
      * *
        *
```

---

# 💻 Program

```python id="4x6y8c"
n = int(input("Enter a number to generate pattern : "))

for i in range(1, n + 1):

    for j in range(1, i - 1 + 1):
        print(" ", end=" ")

    for j in range(1, n - i + 1 + 1):
        print("*", end=" ")

    print(" ")
```

---

# 🧠 Logic of the Program

The program uses one outer loop and two inner loops.

```text id="6r1a5q"
Outer Loop
    ↓
Print Spaces
    ↓
Print Stars
    ↓
Move to Next Row
```

The two important formulas are:

```text id="uhw1ks"
Number of spaces = i - 1
Number of stars  = n - i + 1
```

Therefore:

```text id="gqu4w4"
Spaces increase
Stars decrease
```

---

# 1️⃣ Outer Loop — Controls Rows

```python id="7xuj76"
for i in range(1, n + 1):
```

If:

```text id="k3m3x7"
n = 5
```

then:

```text id="dby8sp"
i = 1, 2, 3, 4, 5
```

So the program creates **5 rows**.

---

# 2️⃣ First Inner Loop — Prints Spaces

```python id="8t8a9e"
for j in range(1, i - 1 + 1):
    print(" ", end=" ")
```

The ending value is:

```text id="l0d3bv"
i - 1 + 1 = i
```

Because `range()` excludes the ending value, the number of iterations is:

```text id="4qgb8q"
i - 1
```

Therefore:

```text id="t5t4jd"
Row 1 → 0 spaces
Row 2 → 1 space
Row 3 → 2 spaces
Row 4 → 3 spaces
Row 5 → 4 spaces
```

This pushes the stars toward the right.

---

# 3️⃣ Second Inner Loop — Prints Stars

```python id="6s4r4k"
for j in range(1, n - i + 1 + 1):
    print("*", end=" ")
```

The number of stars printed is:

```text id="5z5e6e"
n - i + 1
```

For `n = 5`:

```text id="8h3thm"
Row 1 → 5 stars
Row 2 → 4 stars
Row 3 → 3 stars
Row 4 → 2 stars
Row 5 → 1 star
```

---

# 🔍 Example

Suppose the user enters:

```text id="i5d1wh"
Enter a number to generate pattern : 5
```

Then:

```text id="jgl6jp"
n = 5
```

The outer loop runs:

```text id="36epjd"
i = 1, 2, 3, 4, 5
```

---

# 📊 Complete Tracing

## Row 1 — `i = 1`

### Space Loop

```text id="u8gj7d"
i - 1 = 1 - 1 = 0
```

No spaces.

### Star Loop

```text id="q84h3s"
n - i + 1
= 5 - 1 + 1
= 5
```

Prints 5 stars.

```text id="1unfvl"
* * * * *
```

---

## Row 2 — `i = 2`

### Space Loop

```text id="kw8dij"
i - 1 = 2 - 1 = 1
```

Prints 1 space.

### Star Loop

```text id="zldd0v"
5 - 2 + 1 = 4
```

Prints 4 stars.

```text id="0ixbmg"
  * * * *
```

---

## Row 3 — `i = 3`

### Space Loop

```text id="z3r6i1"
3 - 1 = 2
```

Prints 2 spaces.

### Star Loop

```text id="h9g1jn"
5 - 3 + 1 = 3
```

Prints 3 stars.

```text id="zqyg99"
    * * *
```

---

## Row 4 — `i = 4`

### Space Loop

```text id="wibf6u"
4 - 1 = 3
```

Prints 3 spaces.

### Star Loop

```text id="2r7a08"
5 - 4 + 1 = 2
```

Prints 2 stars.

```text id="qx9xkf"
      * *
```

---

## Row 5 — `i = 5`

### Space Loop

```text id="b8e8te"
5 - 1 = 4
```

Prints 4 spaces.

### Star Loop

```text id="k4yn8b"
5 - 5 + 1 = 1
```

Prints 1 star.

```text id="n6yy3g"
        *
```

---

# 📋 Complete Trace Table

| Row `i` | Spaces `i-1` | Stars `n-i+1` | Pattern |
|---:|---:|---:|---|
| 1 | 0 | 5 | `* * * * *` |
| 2 | 1 | 4 | `  * * * *` |
| 3 | 2 | 3 | `    * * *` |
| 4 | 3 | 2 | `      * *` |
| 5 | 4 | 1 | `        *` |

---

# 🔄 Pattern Logic

The pattern follows two opposite sequences.

### Spaces

```text id="w9hdj8"
0 → 1 → 2 → 3 → 4
```

Formula:

```text id="8t1klx"
i - 1
```

### Stars

```text id="uw3pko"
5 → 4 → 3 → 2 → 1
```

Formula:

```text id="d9k7hc"
n - i + 1
```

Therefore:

```text id="u4qkdy"
Increasing Spaces
        +
Decreasing Stars
        ↓
Right-Aligned Inverted Triangle
```

---

# 🖨️ Output

For input:

```text id="c0v5ts"
Enter a number to generate pattern : 5
```

Output:

```text id="q6c99n"
* * * * *
  * * * *
    * * *
      * *
        *
```

---

# 🔄 Program Flow

```text id="5v4l50"
             Input n
                ↓
        Start outer loop
                ↓
             i = 1
                ↓
        Print i-1 spaces
                ↓
      Print n-i+1 stars
                ↓
            New line
                ↓
         Increase i
                ↓
       Repeat until i=n
                ↓
              Stop
```

---

# 📚 Concepts Practiced

- Nested `for` loops
- `range()`
- Pattern programming
- Increasing spaces
- Decreasing stars
- Right alignment
- Loop variables
- `print()` with `end`

## 💡 Key Takeaway

The two main formulas are:

```text id="x1rq6m"
Spaces = i - 1
Stars  = n - i + 1
```

As the rows increase:

```text id="36gcfr"
Spaces ↑
Stars  ↓
```

### In One Line

> **Print `i-1` spaces followed by `n-i+1` stars to create a right-aligned inverted star triangle.**