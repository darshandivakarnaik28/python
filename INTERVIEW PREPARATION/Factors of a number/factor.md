# Find Factors of a Number 🔢

## 📌 Description

This Python program finds all the **factors** of a given number.

A factor of a number is a number that divides it **exactly without leaving a remainder**.

The program checks every number from `1` to `n`.

If:

```python
n % i == 0
```

then `i` is a factor of `n`.

For example, the factors of `12` are:

```text
1 2 3 4 6 12
```

---

# 💻 Program

```python
n = int(input("Enter the number: "))

print("Factors of", n, "is: ", end=" ")

for i in range(1, n + 1):
    if n % i == 0:
        print(i, end=" ")
```

---

# 🧠 Logic of the Program

The main logic is:

```python
if n % i == 0:
```

The `%` operator gives the **remainder** after division.

If the remainder is `0`, it means `i` divides `n` completely.

Therefore:

```text
n % i == 0
       ↓
i is a factor of n
```

---

# 🔍 Example

Suppose the user enters:

```text
Enter the number: 12
```

Then:

```text
n = 12
```

The loop checks:

```text
1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12
```

Each number is tested using:

```text
12 % i
```

---

# 📊 Complete Tracing

| `i` | Calculation | Remainder | Factor? |
|---:|---|---:|:---:|
| 1 | `12 % 1` | 0 | Yes |
| 2 | `12 % 2` | 0 | Yes |
| 3 | `12 % 3` | 0 | Yes |
| 4 | `12 % 4` | 0 | Yes |
| 5 | `12 % 5` | 2 | No |
| 6 | `12 % 6` | 0 | Yes |
| 7 | `12 % 7` | 5 | No |
| 8 | `12 % 8` | 4 | No |
| 9 | `12 % 9` | 3 | No |
| 10 | `12 % 10` | 2 | No |
| 11 | `12 % 11` | 1 | No |
| 12 | `12 % 12` | 0 | Yes |

The factors found are:

```text
1 2 3 4 6 12
```

---

# 🔄 Step-by-Step Working

### Step 1 — Input

```python
n = int(input("Enter the number: "))
```

Suppose:

```text
n = 12
```

### Step 2 — Start the Loop

```python
for i in range(1, n + 1):
```

This checks every number from:

```text
1 → 12
```

### Step 3 — Check Divisibility

```python
if n % i == 0:
```

If the remainder is `0`, the number is a factor.

### Step 4 — Print the Factor

```python
print(i, end=" ")
```

The factor is printed on the same line.

---

# 🖨️ Output

For input:

```text
Enter the number: 12
```

Output:

```text
Factors of 12 is: 1 2 3 4 6 12
```

---

# 🔄 Program Flow

```text
          Input n
             ↓
        i = 1 to n
             ↓
       Calculate n % i
             ↓
     Is remainder = 0?
        /          \
      Yes           No
       ↓             ↓
   Print i        Skip i
       ↓             ↓
       └──────┬──────┘
              ↓
        Next value of i
              ↓
          Repeat
```

---

# 📚 Concepts Practiced

- `for` loop
- `range()`
- `%` modulus operator
- Divisibility
- Factors of a number
- Conditional `if`
- Basic number logic

## 💡 Key Takeaway

The core logic is:

```python
if n % i == 0:
```

If the remainder is `0`, `i` is a factor of `n`.

### In One Line

> **Check every number from `1` to `n`; if `n % i` is `0`, print `i` because it is a factor of `n`.**