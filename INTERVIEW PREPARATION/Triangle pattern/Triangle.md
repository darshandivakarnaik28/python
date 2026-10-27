# Right-Angled Star Triangle ⭐

## 📌 Description

This Python program generates a **right-angled triangle pattern** using nested `for` loops.

The number of stars starts from `1` and increases by `1` in every row.

For example, if `n = 5`:

```text
*
* *
* * *
* * * *
* * * * *
```

---

# 💻 Program

```python
n = int(input("Enter a number to generate triangle : "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()
```

---

# 🧠 Logic of the Program

The program uses **two nested loops**.

### Outer Loop

```python
for i in range(1, n + 1):
```

The outer loop controls the **number of rows**.

If:

```text
n = 5
```

then:

```text
i = 1, 2, 3, 4, 5
```

So the program creates 5 rows.

### Inner Loop

```python
for j in range(1, i + 1):
    print("*", end=" ")
```

The inner loop prints the stars.

The number of stars is equal to the current row number:

```text
Number of stars = i
```

Therefore:

```text
Row 1 → 1 star
Row 2 → 2 stars
Row 3 → 3 stars
Row 4 → 4 stars
Row 5 → 5 stars
```

---

# 🔍 Example

Suppose the user enters:

```text
Enter a number to generate triangle : 5
```

Then:

```text
n = 5
```

The outer loop runs:

```text
i = 1, 2, 3, 4, 5
```

For each `i`, the inner loop prints `i` stars.

---

# 📊 Complete Tracing

## Row 1 — `i = 1`

Inner loop:

```text
j = 1
```

One star is printed:

```text
*
```

---

## Row 2 — `i = 2`

Inner loop:

```text
j = 1 → *
j = 2 → *
```

Output:

```text
* *
```

---

## Row 3 — `i = 3`

Inner loop:

```text
j = 1 → *
j = 2 → *
j = 3 → *
```

Output:

```text
* * *
```

---

## Row 4 — `i = 4`

Inner loop:

```text
j = 1 → *
j = 2 → *
j = 3 → *
j = 4 → *
```

Output:

```text
* * * *
```

---

## Row 5 — `i = 5`

Inner loop:

```text
j = 1 → *
j = 2 → *
j = 3 → *
j = 4 → *
j = 5 → *
```

Output:

```text
* * * * *
```

---

# 📋 Complete Trace Table

| Row `i` | `j` values | Number of Stars | Output |
|---:|---|---:|---|
| 1 | 1 | 1 | `*` |
| 2 | 1, 2 | 2 | `* *` |
| 3 | 1, 2, 3 | 3 | `* * *` |
| 4 | 1, 2, 3, 4 | 4 | `* * * *` |
| 5 | 1, 2, 3, 4, 5 | 5 | `* * * * *` |

---

# 🔄 Pattern Logic

The number of stars follows:

```text
1 → 2 → 3 → 4 → 5
```

So:

```text
Number of stars = i
```

The pattern grows by one star in every row.

```text
Row 1 → *
Row 2 → * *
Row 3 → * * *
Row 4 → * * * *
Row 5 → * * * * *
```

---

# 🖨️ Output

For input:

```text
5
```

Output:

```text
*
* *
* * *
* * * *
* * * * *
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
      Start inner loop
                ↓
          Print i stars
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
- Increasing number of stars
- Rows and columns
- `print()` with `end`
- Loop variables

## 💡 Key Takeaway

The important relationship is:

```text
Number of rows = n
Number of stars in row = i
```

As `i` increases, the number of stars also increases.

### In One Line

> **Print `i` stars for every row `i` from `1` to `n` to generate a right-angled star triangle.**