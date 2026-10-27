# Reverse Odd Numbers 🔄🔢

## 📌 Description

This Python program generates the **odd numbers** up to a given range and then prints those odd numbers in reverse order.

The program does not use the `%` operator to check whether a number is odd.

It directly generates odd numbers using:

```python
i + i - 1
```

For reversing the odd numbers, it uses:

```python
n - i + n - i + 1
```

For example, if the input is:

```text
10
```

the output is:

```text
Before Reverse:1 3 5 7 9
After Reverse:9 7 5 3 1
```

---

# 💻 Program

```python
n = int(input("Enter a range to generate Reverse odd number : "))

n = int(n / 2)

print("Before Reverse:", end="")

for i in range(1, n + 1):
    print(i + i - 1, end=" ")

print("\nAfter Reverse:", end="")

for i in range(1, n + 1):
    print(n - i + n - i + 1, end=" ")
```

---

# 🧠 Logic of the Program

The program works in three steps:

1. Find how many odd numbers are present in the given range.
2. Generate the odd numbers in normal order.
3. Generate the same odd numbers in reverse order.

---

# 1️⃣ Find the Number of Odd Numbers

```python
n = int(n / 2)
```

Suppose the input is:

```text
n = 10
```

Then:

```text
n = int(10 / 2)
n = 5
```

There are 5 odd numbers from `1` to `10`:

```text
1, 3, 5, 7, 9
```

So now `n = 5` represents the **number of odd numbers**.

---

# 2️⃣ Generate Odd Numbers

The first loop is:

```python
for i in range(1, n + 1):
    print(i + i - 1, end=" ")
```

The expression:

```text
i + i - 1
```

is the same as:

```text
2i - 1
```

This generates odd numbers.

For example:

```text
i = 1 → 1 + 1 - 1 = 1
i = 2 → 2 + 2 - 1 = 3
i = 3 → 3 + 3 - 1 = 5
i = 4 → 4 + 4 - 1 = 7
i = 5 → 5 + 5 - 1 = 9
```

Therefore:

```text
1 3 5 7 9
```

---

# 3️⃣ Generate Reverse Odd Numbers

The second loop uses:

```python
print(n - i + n - i + 1, end=" ")
```

The expression is:

```text
n - i + n - i + 1
```

Simplifying:

```text
2n - 2i + 1
```

or:

```text
2(n - i) + 1
```

This generates the odd numbers from largest to smallest.

---

# 🔍 Example

Suppose the user enters:

```text
Enter a range to generate Reverse odd number : 10
```

Initially:

```text
n = 10
```

After:

```python
n = int(n / 2)
```

we get:

```text
n = 5
```

The loop runs:

```text
i = 1, 2, 3, 4, 5
```

---

# 📊 Complete Tracing — Before Reverse

The formula is:

```text
i + i - 1
```

| Step | `i` | Calculation | Output |
|---:|---:|---|---:|
| 1 | 1 | `1 + 1 - 1` | 1 |
| 2 | 2 | `2 + 2 - 1` | 3 |
| 3 | 3 | `3 + 3 - 1` | 5 |
| 4 | 4 | `4 + 4 - 1` | 7 |
| 5 | 5 | `5 + 5 - 1` | 9 |

Therefore:

```text
Before Reverse:1 3 5 7 9
```

---

# 📊 Complete Tracing — After Reverse

The formula is:

```text
n - i + n - i + 1
```

Here:

```text
n = 5
```

### Step 1 — `i = 1`

```text
5 - 1 + 5 - 1 + 1
= 4 + 4 + 1
= 9
```

Output:

```text
9
```

---

### Step 2 — `i = 2`

```text
5 - 2 + 5 - 2 + 1
= 3 + 3 + 1
= 7
```

Output:

```text
7
```

---

### Step 3 — `i = 3`

```text
5 - 3 + 5 - 3 + 1
= 2 + 2 + 1
= 5
```

Output:

```text
5
```

---

### Step 4 — `i = 4`

```text
5 - 4 + 5 - 4 + 1
= 1 + 1 + 1
= 3
```

Output:

```text
3
```

---

### Step 5 — `i = 5`

```text
5 - 5 + 5 - 5 + 1
= 0 + 0 + 1
= 1
```

Output:

```text
1
```

Therefore:

```text
After Reverse:9 7 5 3 1
```

---

# 📋 Complete Trace Table

| `i` | Before: `i+i-1` | After: `n-i+n-i+1` |
|---:|---:|---:|
| 1 | 1 | 9 |
| 2 | 3 | 7 |
| 3 | 5 | 5 |
| 4 | 7 | 3 |
| 5 | 9 | 1 |

---

# 🔄 Pattern of the Program

### Before Reverse

```text
1 → 3 → 5 → 7 → 9
```

Each number increases by `2`.

### After Reverse

```text
9 → 7 → 5 → 3 → 1
```

Each number decreases by `2`.

Therefore:

```text
Before: 1  3  5  7  9
         ↓  ↓  ↓  ↓  ↓
After:  9  7  5  3  1
```

---

# 🧮 Understanding the Formulas

### Normal Odd Number

Your formula:

```text
i + i - 1
```

is equivalent to:

```text
2i - 1
```

Therefore:

```text
i = 1 → 1
i = 2 → 3
i = 3 → 5
```

---

### Reverse Odd Number

Your formula:

```text
n - i + n - i + 1
```

is equivalent to:

```text
2(n-i) + 1
```

For `n = 5`:

```text
i = 1 → 2(5-1)+1 = 9
i = 2 → 2(5-2)+1 = 7
i = 3 → 2(5-3)+1 = 5
i = 4 → 2(5-4)+1 = 3
i = 5 → 2(5-5)+1 = 1
```

So it produces:

```text
9 7 5 3 1
```

---

# 🖨️ Output

For input:

```text
Enter a range to generate Reverse odd number : 10
```

Output:

```text
Before Reverse:1 3 5 7 9
After Reverse:9 7 5 3 1
```

---

# 🔄 Program Flow

```text
             Input range
                  ↓
              n = n / 2
                  ↓
       Number of odd numbers
                  ↓
        ┌─────────┴─────────┐
        ↓                   ↓
 Generate normal        Generate reverse
   odd numbers            odd numbers
        ↓                   ↓
    i+i-1             n-i+n-i+1
        ↓                   ↓
  1 3 5 7 9            9 7 5 3 1
```

---

# 📚 Concepts Practiced

- Python `for` loop
- `range()`
- Arithmetic expressions
- Odd number generation
- Reverse sequence generation
- Mathematical formulas
- Loop-based number generation

## 💡 Key Takeaway

The program uses:

```python
i + i - 1
```

to generate:

```text
1 3 5 7 9
```

and:

```python
n - i + n - i + 1
```

to generate:

```text
9 7 5 3 1
```

### In One Line

> **First generate odd numbers using `2i-1`, then generate the same odd numbers in reverse using `2(n-i)+1`.**