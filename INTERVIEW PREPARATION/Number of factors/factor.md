# Count Total Factors of a Number 🔢

## 📌 Description

This Python program finds the **total number of factors** of a given number.

Instead of printing the factors, the program uses a `count` variable to keep track of how many factors the number has.

The main condition is:

```python
if n % i == 0:
```

If the remainder is `0`, then `i` is a factor of `n`, so:

```python
count += 1
```

is used to increase the factor count.

---

# 💻 Program

```python
n = int(input("Enter the number: "))

print("Total Factors of", n, "is:", end=" ")

count = 0

for i in range(1, n + 1):
    if n % i == 0:
        count += 1

print(count)
```

---

# 🧠 Logic of the Program

The program works in three main steps:

1. Take a number as input.
2. Check every number from `1` to `n` to see whether it is a factor.
3. Increase `count` whenever a factor is found.

The main logic is:

```python
if n % i == 0:
    count += 1
```

This means:

```text
If i divides n completely
        ↓
i is a factor
        ↓
Increase count by 1
```

---

# 🔍 Example

Suppose the user enters:

```text
Enter the number: 12
```

The factors of `12` are:

```text
1, 2, 3, 4, 6, 12
```

Therefore, the total number of factors is:

```text
6
```

---

# 📊 Complete Tracing

For:

```text
n = 12
```

Initially:

```text
count = 0
```

The loop checks every value from `1` to `12`.

| `i` | `12 % i` | Factor? | `count` |
|---:|---:|:---:|---:|
| 1 | 0 | Yes | 1 |
| 2 | 0 | Yes | 2 |
| 3 | 0 | Yes | 3 |
| 4 | 0 | Yes | 4 |
| 5 | 2 | No | 4 |
| 6 | 0 | Yes | 5 |
| 7 | 5 | No | 5 |
| 8 | 4 | No | 5 |
| 9 | 3 | No | 5 |
| 10 | 2 | No | 5 |
| 11 | 1 | No | 5 |
| 12 | 0 | Yes | 6 |

Finally:

```text
count = 6
```

Output:

```text
Total Factors of 12 is: 6
```

---

# 🔄 Step-by-Step Working

### Step 1 — Take Input

```python
n = int(input("Enter the number: "))
```

Suppose:

```text
n = 12
```

### Step 2 — Initialize Count

```python
count = 0
```

Initially, no factors have been found.

```text
count = 0
```

### Step 3 — Check Every Number

```python
for i in range(1, n + 1):
```

The values of `i` are:

```text
1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12
```

### Step 4 — Check Whether It Is a Factor

```python
if n % i == 0:
```

If the remainder is `0`, then `i` is a factor.

### Step 5 — Increase Count

```python
count += 1
```

Every time a factor is found, the count increases by `1`.

---

# 🧮 Example of Count Changes

For `n = 12`:

```text
Start       → count = 0

i = 1       → factor → count = 1
i = 2       → factor → count = 2
i = 3       → factor → count = 3
i = 4       → factor → count = 4
i = 5       → not factor → count = 4
i = 6       → factor → count = 5
i = 7       → not factor → count = 5
i = 8       → not factor → count = 5
i = 9       → not factor → count = 5
i = 10      → not factor → count = 5
i = 11      → not factor → count = 5
i = 12      → factor → count = 6
```

Final:

```text
count = 6
```

---

# 🔄 Program Flow

```text
          Input n
             ↓
        count = 0
             ↓
        i = 1 to n
             ↓
       Calculate n % i
             ↓
     Is remainder = 0?
        /          \
      Yes           No
       ↓             ↓
 count += 1        Skip
       ↓             ↓
       └──────┬──────┘
              ↓
        Next value of i
              ↓
           Repeat
              ↓
        Print count
```

---

# 🖨️ Output

For input:

```text
Enter the number: 12
```

Output:

```text
Total Factors of 12 is: 6
```

---

# 🔗 Relation to Your Prime Number Program

This program is directly related to your previous **prime number program**.

In your prime-number logic, you first count the factors:

```python
count += 1
```

Then:

```python
if count == 2:
    print("Prime Number")
```

A prime number has exactly **2 factors**:

```text
1 and itself
```

So this program is the **factor-counting part** that can be used to determine whether a number is prime.

For example:

```text
12 → 6 factors → Not Prime
7  → 2 factors → Prime
```

## 💡 Key Takeaway

> **Check every number from `1` to `n`. Whenever `n % i == 0`, increase `count`. At the end, `count` gives the total number of factors of `n`.**