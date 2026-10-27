# Reverse a Range of Numbers 🔄

## 📌 Description

This Python program prints a range of numbers from `1` to `n` and then prints the same numbers in reverse order.

For example, if the user enters:

```text
5
```

The program prints:

```text
Before Reverse: 1 2 3 4 5
After Reverse: 5 4 3 2 1
```

The reverse is generated using the formula:

```python
n - i + 1
```

---

# 💻 Program

```python
n = int(input("Enter a range to reverse : "))

print("Before Reverse:", end="")

for i in range(1, n + 1):
    print(i, end=" ")

print("\nAfter Reverse:", end="")

for i in range(1, n + 1):
    print(n - i + 1, end=" ")
```

---

# 🧠 Logic of the Program

The program has **two `for` loops**.

### 1. Print the Original Range

```python
for i in range(1, n + 1):
    print(i, end=" ")
```

If:

```text
n = 5
```

then:

```text
range(1, 6)
```

generates:

```text
1 2 3 4 5
```

So the output is:

```text
Before Reverse: 1 2 3 4 5
```

---

### 2. Print the Range in Reverse

The second loop uses:

```python
n - i + 1
```

For every value of `i`, this formula gives the corresponding number from the end.

For:

```text
n = 5
```

we get:

```text
i = 1 → 5 - 1 + 1 = 5
i = 2 → 5 - 2 + 1 = 4
i = 3 → 5 - 3 + 1 = 3
i = 4 → 5 - 4 + 1 = 2
i = 5 → 5 - 5 + 1 = 1
```

Therefore:

```text
5 4 3 2 1
```

---

# 🔍 Example

Suppose the user enters:

```text
Enter a range to reverse : 5
```

Then:

```text
n = 5
```

---

# 📊 Complete Tracing

## First Loop — Before Reverse

The loop is:

```python
for i in range(1, n + 1):
```

Since `n = 5`:

```text
range(1, 6)
```

| Step | `i` | Printed |
|---:|---:|---:|
| 1 | 1 | 1 |
| 2 | 2 | 2 |
| 3 | 3 | 3 |
| 4 | 4 | 4 |
| 5 | 5 | 5 |

Output:

```text
Before Reverse: 1 2 3 4 5
```

---

# 🔄 Second Loop — After Reverse

The formula is:

```python
n - i + 1
```

Since `n = 5`:

| Step | `i` | Calculation | Printed |
|---:|---:|---|---:|
| 1 | 1 | `5 - 1 + 1` | 5 |
| 2 | 2 | `5 - 2 + 1` | 4 |
| 3 | 3 | `5 - 3 + 1` | 3 |
| 4 | 4 | `5 - 4 + 1` | 2 |
| 5 | 5 | `5 - 5 + 1` | 1 |

Output:

```text
After Reverse: 5 4 3 2 1
```

---

# 🧮 Understanding `n - i + 1`

This is the main logic of the program.

For:

```text
n = 5
```

we want:

```text
5 4 3 2 1
```

As `i` increases:

```text
i = 1 → 5
i = 2 → 4
i = 3 → 3
i = 4 → 2
i = 5 → 1
```

The formula:

```text
n - i + 1
```

produces exactly this sequence.

### Why `+1`?

Without `+1`:

```text
5 - 1 = 4
```

But we need the first value to be `5`.

So:

```text
5 - 1 + 1 = 5
```

The `+1` adjusts the result to start from `n`.

---

# 🖨️ Output

For input:

```text
Enter a range to reverse : 5
```

Output:

```text
Before Reverse:1 2 3 4 5
After Reverse:5 4 3 2 1
```

---

# 🔄 Program Flow

```text
             Input n
                ↓
       Print numbers 1 to n
                ↓
      1  2  3  4  5
                ↓
       Start second loop
                ↓
      Calculate n-i+1
                ↓
      5  4  3  2  1
                ↓
              Stop
```

---

# 📚 Concepts Practiced

- Python input
- `for` loop
- `range()`
- Arithmetic expressions
- Reverse sequence generation
- Loop indexing
- `print()` with `end`

## 💡 Key Takeaway

The original range is generated using:

```python
range(1, n + 1)
```

The reverse range is generated using:

```python
n - i + 1
```

For example:

```text
n = 5

Before:
1 2 3 4 5

After:
5 4 3 2 1
```

### In One Line

> **Print `1` to `n` normally, then use `n - i + 1` to generate the same range in reverse order.**