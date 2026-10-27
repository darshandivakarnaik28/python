# Reverse Even Numbers 🔄🔢

## 📌 Description

This Python program generates the even numbers up to a given range and then prints the same even numbers in reverse order.

The program does not use the `%` operator to find even numbers.

It uses:

```python
i + i
```

to generate even numbers.

For reversing the even numbers, it uses:

```python
n - i + n - i + 2
```

which can be simplified as:

```text
2(n - i + 1)
```

For example, if the input is:

```text
10
```

the output is:

```text
Before Reverse :2 4 6 8 10
After Reverse :10 8 6 4 2
```

---

# 💻 Program

```python
n = int(input("Enter the range to reverse even numbers : "))

n = int(n / 2)

print("Before Reverse :", end="")

for i in range(1, n + 1):
    print(i + i, end=" ")

print("\nAfter Reverse :", end="")

for i in range(1, n + 1):
    print(n - i + n - i + 2, end=" ")
```

---

# 🧠 Logic of the Program

The program works in three main steps:

1. Find how many even numbers exist in the given range.
2. Generate the even numbers in normal order.
3. Generate the same even numbers in reverse order.

---

# 1️⃣ Find the Number of Even Numbers

```python
n = int(n / 2)
```

Suppose the input is:

```text
10
```

Then:

```text
n = 10
n = int(10 / 2)
n = 5
```

There are 5 even numbers from `1` to `10`:

```text
2, 4, 6, 8, 10
```

So now `n = 5` represents the **number of even numbers**, not the original range.

---

# 2️⃣ Generate Even Numbers

The first loop is:

```python
for i in range(1, n + 1):
    print(i + i, end=" ")
```

The expression:

```text
i + i
```

is the same as:

```text
2 × i
```

Therefore:

```text
i = 1 → 1 + 1 = 2
i = 2 → 2 + 2 = 4
i = 3 → 3 + 3 = 6
i = 4 → 4 + 4 = 8
i = 5 → 5 + 5 = 10
```

So:

```text
2 4 6 8 10
```

---

# 3️⃣ Reverse the Even Numbers

The second loop is:

```python
for i in range(1, n + 1):
    print(n - i + n - i + 2, end=" ")
```

The expression is:

```text
n - i + n - i + 2
```

Combine the terms:

```text
n + n - i - i + 2
```

Therefore:

```text
2n - 2i + 2
```

or:

```text
2(n - i + 1)
```

This produces the even numbers from the largest to the smallest.

---

# 🔍 Example

Suppose:

```text
Enter the range to reverse even numbers : 10
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

Now the program considers there are:

```text
5 even numbers
```

---

# 📊 Complete Tracing — Before Reverse

The loop is:

```python
for i in range(1, n + 1):
```

Since `n = 5`:

```text
range(1, 6)
```

So `i` becomes:

```text
1, 2, 3, 4, 5
```

| Step | `i` | Calculation | Output |
|---:|---:|---|---:|
| 1 | 1 | `1 + 1` | 2 |
| 2 | 2 | `2 + 2` | 4 |
| 3 | 3 | `3 + 3` | 6 |
| 4 | 4 | `4 + 4` | 8 |
| 5 | 5 | `5 + 5` | 10 |

Therefore:

```text
Before Reverse :2 4 6 8 10
```

---

# 📊 Complete Tracing — After Reverse

The formula is:

```text
n - i + n - i + 2
```

Here:

```text
n = 5
```

### Step 1 — `i = 1`

```text
5 - 1 + 5 - 1 + 2
= 4 + 4 + 2
= 10
```

Output:

```text
10
```

---

### Step 2 — `i = 2`

```text
5 - 2 + 5 - 2 + 2
= 3 + 3 + 2
= 8
```

Output:

```text
8
```

---

### Step 3 — `i = 3`

```text
5 - 3 + 5 - 3 + 2
= 2 + 2 + 2
= 6
```

Output:

```text
6
```

---

### Step 4 — `i = 4`

```text
5 - 4 + 5 - 4 + 2
= 1 + 1 + 2
= 4
```

Output:

```text
4
```

---

### Step 5 — `i = 5`

```text
5 - 5 + 5 - 5 + 2
= 0 + 0 + 2
= 2
```

Output:

```text
2
```

Therefore:

```text
After Reverse :10 8 6 4 2
```

---

# 📋 Complete Trace Table

| `i` | Before: `i+i` | After: `n-i+n-i+2` |
|---:|---:|---:|
| 1 | 2 | 10 |
| 2 | 4 | 8 |
| 3 | 6 | 6 |
| 4 | 8 | 4 |
| 5 | 10 | 2 |

---

# 🔄 Pattern of the Program

### Before Reverse

```text
2 → 4 → 6 → 8 → 10
```

Each number increases by `2`.

### After Reverse

```text
10 → 8 → 6 → 4 → 2
```

Each number decreases by `2`.

So:

```text
Before:  2   4   6   8   10
          ↓   ↓   ↓   ↓    ↓
After:  10   8   6   4    2
```

---

# 🧮 Understanding the Reverse Formula

Your expression:

```python
n - i + n - i + 2
```

can be simplified:

```text
n - i + n - i + 2
= 2n - 2i + 2
= 2(n - i + 1)
```

For `n = 5`:

```text
i = 1 → 2(5 - 1 + 1) = 10
i = 2 → 2(5 - 2 + 1) = 8
i = 3 → 2(5 - 3 + 1) = 6
i = 4 → 2(5 - 4 + 1) = 4
i = 5 → 2(5 - 5 + 1) = 2
```

Thus, the formula generates the even numbers in reverse.

---

# 🖨️ Output

For input:

```text
Enter the range to reverse even numbers : 10
```

Output:

```text
Before Reverse :2 4 6 8 10
After Reverse :10 8 6 4 2
```

---

# 🔄 Program Flow

```text
              Input range
                   ↓
              n = n / 2
                   ↓
       Number of even values
                   ↓
        ┌──────────┴──────────┐
        ↓                     ↓
  Generate normal       Generate reverse
       even numbers         even numbers
        ↓                     ↓
      i + i          n-i+n-i+2
        ↓                     ↓
  2 4 6 8 10          10 8 6 4 2
```

---

# 📚 Concepts Practiced

- Python `for` loop
- `range()`
- Arithmetic expressions
- Even number generation
- Reverse sequence generation
- Mathematical formulas
- Loop-based pattern generation

## 💡 Key Takeaway

The program uses:

```python
i + i
```

to generate even numbers:

```text
2, 4, 6, 8, 10
```

and:

```python
n - i + n - i + 2
```

to generate them in reverse:

```text
10, 8, 6, 4, 2
```

### In One Line

> **First generate the even numbers using `i+i`, then use `n-i+n-i+2` to generate the same even numbers in reverse order.**