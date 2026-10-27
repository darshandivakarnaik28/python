# Inverted Star Triangle ⭐

## 📌 Description

This Python program generates an **inverted right-angled triangle pattern** using nested `for` loops.

The first row contains `n` stars. In every next row, the number of stars decreases by `1`.

For example, if:

```text
n = 5
```

the output is:

```text
* * * * *
* * * *
* * *
* *
*
```

---

# 💻 Program

```python
n = int(input("Enter a size for generate triangle : "))

for i in range(1, n + 1):

    for j in range(1, n - i + 1 + 1, 1):
        print("*", end=" ")

    print()
```

---

# 🧠 Logic of the Program

The program uses:

- One **outer loop** to control the rows.
- One **inner loop** to print the stars.

The important expression is:

```python
n - i + 1 + 1
```

which simplifies to:

```text
n - i + 2
```

Because `range()` does not include its ending value, the number of stars printed is:

```text
n - i + 1
```

So the number of stars decreases as `i` increases.

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

Therefore, the program generates **5 rows**.

---

# 2️⃣ Inner Loop — Prints Stars

```python
for j in range(1, n - i + 1 + 1, 1):
    print("*", end=" ")
```

The number of stars is:

```text
n - i + 1
```

For `n = 5`:

```text
i = 1 → 5 stars
i = 2 → 4 stars
i = 3 → 3 stars
i = 4 → 2 stars
i = 5 → 1 star
```

Therefore, the triangle is inverted.

---

# 🔍 Example

Suppose the user enters:

```text
Enter a size for generate triangle : 5
```

Then:

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

Number of stars:

```text
n - i + 1
= 5 - 1 + 1
= 5
```

Output:

```text
* * * * *
```

---

## Row 2 — `i = 2`

```text
5 - 2 + 1 = 4
```

Output:

```text
* * * *
```

---

## Row 3 — `i = 3`

```text
5 - 3 + 1 = 3
```

Output:

```text
* * *
```

---

## Row 4 — `i = 4`

```text
5 - 4 + 1 = 2
```

Output:

```text
* *
```

---

## Row 5 — `i = 5`

```text
5 - 5 + 1 = 1
```

Output:

```text
*
```

---

# 📋 Complete Trace Table

| Row `i` | Star Count `n-i+1` | Output |
|---:|---:|---|
| 1 | 5 | `* * * * *` |
| 2 | 4 | `* * * *` |
| 3 | 3 | `* * *` |
| 4 | 2 | `* *` |
| 5 | 1 | `*` |

---

# 🔄 Pattern Logic

The number of stars follows:

```text
5 → 4 → 3 → 2 → 1
```

So:

```text
Stars = n - i + 1
```

The stars decrease by one after every row.

```text
Row 1 → * * * * *
Row 2 → * * * *
Row 3 → * * *
Row 4 → * *
Row 5 → *
```

---

# 🖨️ Output

For:

```text
n = 5
```

Output:

```text
* * * * *
* * * *
* * *
* *
*
```

---

# 🔄 Program Flow

```text
             Input n
                ↓
         Start outer loop
                ↓
             i = 1
                ↓
       Calculate n-i+1
                ↓
        Print that many *
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
- Decreasing sequence
- Loop variables
- `print()` with `end`
- Star patterns

## 💡 Key Takeaway

The main formula is:

```text
Number of stars = n - i + 1
```

As the row number `i` increases, the number of stars decreases.

### In One Line

> **Print `n-i+1` stars in every row to create an inverted right-angled triangle.**