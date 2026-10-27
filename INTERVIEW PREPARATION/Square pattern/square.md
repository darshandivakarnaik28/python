# Square Star Pattern ⭐

## 📌 Description

This Python program generates a **square pattern of stars** using nested `for` loops.

The user enters the size of the square. The program then prints:

- `n` rows
- `n` stars in each row

Therefore, the total number of stars is:

```text
n × n
```

For example, if `n = 4`:

```text
* * * *
* * * *
* * * *
* * * *
```

---

# 💻 Program

```python
n = int(input("Enter a number for generate square : "))

for i in range(1, n + 1):
    for j in range(1, n + 1):
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

### Inner Loop

```python
for j in range(1, n + 1):
    print("*", end=" ")
```

The inner loop controls the **number of stars in each row**.

Since both loops run `n` times:

```text
Rows    = n
Columns = n
```

Therefore, the output is a square.

---

# 🔍 Example

Suppose the user enters:

```text
Enter a number for generate square : 4
```

Then:

```text
n = 4
```

The outer loop runs:

```text
i = 1, 2, 3, 4
```

For every value of `i`, the inner loop runs:

```text
j = 1, 2, 3, 4
```

So each row contains 4 stars.

---

# 📊 Complete Tracing

## Row 1 — `i = 1`

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

## Row 2 — `i = 2`

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

## Row 3 — `i = 3`

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

# 📋 Complete Trace Table

For `n = 4`:

| Row `i` | `j` values | Number of Stars |
|---:|---|---:|
| 1 | 1, 2, 3, 4 | 4 |
| 2 | 1, 2, 3, 4 | 4 |
| 3 | 1, 2, 3, 4 | 4 |
| 4 | 1, 2, 3, 4 | 4 |

Total stars:

```text
4 × 4 = 16
```

---

# 🔄 Understanding the Nested Loops

The outer loop decides **which row** we are printing.

```text
i = 1 → Row 1
i = 2 → Row 2
i = 3 → Row 3
i = 4 → Row 4
```

For every row, the inner loop prints 4 stars:

```text
j = 1 → *
j = 2 → *
j = 3 → *
j = 4 → *
```

After the inner loop finishes:

```python
print()
```

moves the cursor to the next line.

---

# 🖨️ Output

For:

```text
n = 4
```

Output:

```text
* * * *
* * * *
* * * *
* * * *
```

---

# 🔄 Program Flow

```text
             Input n
                ↓
        Start outer loop
                ↓
          Select a row
                ↓
       Start inner loop
                ↓
         Print n stars
                ↓
          New line
                ↓
        Next row
                ↓
       Repeat n times
                ↓
              Stop
```

---

# 📚 Concepts Practiced

- Nested `for` loops
- `range()`
- Pattern programming
- Rows and columns
- Square patterns
- `print()` with `end`
- Loop control

## 💡 Key Takeaway

The important idea is:

```text
Outer loop  → Number of rows
Inner loop  → Number of stars per row
```

Both are controlled by `n`:

```text
Rows    = n
Columns = n
```

Therefore:

```text
Total stars = n × n
```

### In One Line

> **Use two nested loops, each running `n` times, to print an `n × n` square of stars.**