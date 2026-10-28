# Combination Pattern ⭐➕

## 📌 Description

This Python program generates a **combination pattern** using two symbols:

- `*` — increases in every row.
- `+` — decreases in every row.

The program uses **nested `for` loops** to generate the pattern.

For example, if the input is `5`, the output is:

```text
* + + + +
* * + + +
* * * + +
* * * * +
* * * * *
```

The important idea is:

```text
Number of * = row number
Number of + = n - row number
```

Therefore, every row contains exactly `n` symbols.

---

# 💻 Program

```python
n = int(input("Enter the number to generate pattern : "))

for i in range(1, n + 1):

    for j in range(1, i + 1):
        print("*", end=" ")

    for j in range(1, n - i + 1):
        print("+", end=" ")

    print()
```

---

# 🧠 Logic of the Program

The program has **three main parts**:

### 1. Outer Loop — Controls Rows

```python
for i in range(1, n + 1):
```

This loop decides how many rows are generated.

If:

```text
n = 5
```

then:

```text
i = 1, 2, 3, 4, 5
```

So there are **5 rows**.

---

### 2. First Inner Loop — Prints `*`

```python
for j in range(1, i + 1):
    print("*", end=" ")
```

The number of `*` depends on `i`.

```text
Row 1 → 1 *
Row 2 → 2 *
Row 3 → 3 *
Row 4 → 4 *
Row 5 → 5 *
```

So the number of stars **increases by one in every row**.

---

### 3. Second Inner Loop — Prints `+`

```python
for j in range(1, n - i + 1):
    print("+", end=" ")
```

The number of `+` depends on:

```text
n - i
```

As `i` increases, the number of `+` decreases.

For `n = 5`:

```text
Row 1 → 4 +
Row 2 → 3 +
Row 3 → 2 +
Row 4 → 1 +
Row 5 → 0 +
```

---

# 🔍 Example

Suppose:

```text
Enter the number to generate pattern : 5
```

Then:

```text
n = 5
```

The outer loop generates:

```text
i = 1
i = 2
i = 3
i = 4
i = 5
```

---

# 📊 Complete Tracing

## Row 1 — `i = 1`

### First loop

```text
range(1, 2)
```

Prints:

```text
*
```

Number of `*`:

```text
1
```

### Second loop

```text
range(1, 5)
```

Prints:

```text
+ + + +
```

Number of `+`:

```text
4
```

Row:

```text
* + + + +
```

---

## Row 2 — `i = 2`

### First loop

```text
range(1, 3)
```

Prints:

```text
* *
```

Number of `*`:

```text
2
```

### Second loop

```text
range(1, 4)
```

Prints:

```text
+ + +
```

Number of `+`:

```text
3
```

Row:

```text
* * + + +
```

---

## Row 3 — `i = 3`

### First loop

Prints:

```text
* * *
```

Number of `*`:

```text
3
```

### Second loop

Prints:

```text
+ +
```

Number of `+`:

```text
2
```

Row:

```text
* * * + +
```

---

## Row 4 — `i = 4`

First loop:

```text
* * * *
```

Second loop:

```text
+
```

Row:

```text
* * * * +
```

---

## Row 5 — `i = 5`

First loop:

```text
* * * * *
```

Second loop:

```text
```

No `+` symbols are printed.

Row:

```text
* * * * *
```

---

# 📋 Trace Table

| Row `i` | Number of `*` | Number of `+` | Final Row |
|---:|---:|---:|---|
| 1 | 1 | 4 | `* + + + +` |
| 2 | 2 | 3 | `* * + + +` |
| 3 | 3 | 2 | `* * * + +` |
| 4 | 4 | 1 | `* * * * +` |
| 5 | 5 | 0 | `* * * * *` |

---

# 🔄 Pattern Logic

The pattern follows:

```text
Row 1 → 1 star  + 4 plus
Row 2 → 2 stars + 3 plus
Row 3 → 3 stars + 2 plus
Row 4 → 4 stars + 1 plus
Row 5 → 5 stars + 0 plus
```

Therefore:

```text
Stars = i
Plus  = n - i
```

And:

```text
Stars + Plus = n
```

For every row:

```text
1 + 4 = 5
2 + 3 = 5
3 + 2 = 5
4 + 1 = 5
5 + 0 = 5
```

---

# 🖨️ Output

For:

```text
n = 5
```

Output:

```text
* + + + +
* * + + +
* * * + +
* * * * +
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
        Print i number of *
                 ↓
       Print n-i number of +
                 ↓
              New line
                 ↓
          Next row (i++)
                 ↓
             i > n?
             ↙   ↘
           No     Yes
            ↓      ↓
        Repeat    Stop
```

---

# 📚 Concepts Practiced

- Nested `for` loops
- `range()`
- Pattern programming
- Loop variables
- Arithmetic expressions
- Increasing pattern
- Decreasing pattern
- `print()` with `end`

## 💡 Key Takeaway

The main logic is:

```python
for j in range(1, i + 1):
```

→ prints **increasing `*`**.

```python
for j in range(1, n - i + 1):
```

→ prints **decreasing `+`**.

So the combination pattern is created by combining:

```text
Increasing pattern + Decreasing pattern
```

### In One Line

> **For each row, print `i` stars followed by `n-i` plus symbols.**