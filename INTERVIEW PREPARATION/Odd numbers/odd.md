# Generate Odd Numbers 🔢

## 📌 Description

This Python program generates the **odd numbers** from `1` up to the given range.

Instead of checking whether each number is odd using the `%` operator, the program directly generates odd numbers using the formula:

```text
2 × i - 1
```

The program writes this formula as:

```python
i + i - 1
```

For example, if the input is:

```text
10
```

the output is:

```text
1
3
5
7
9
```

---

# 💻 Program

```python
n = int(input("Enter a range to generate odd numbers : "))

n = int(n / 2)

for i in range(1, n + 1):
    print(i + i - 1)
```

---

# 🧠 Logic of the Program

The program works in two steps.

### Step 1 — Find the Number of Odd Numbers

```python
n = int(n / 2)
```

For example:

```text
n = 10
```

Then:

```text
10 / 2 = 5
```

So:

```text
n = 5
```

There are 5 odd numbers from `1` to `10`:

```text
1, 3, 5, 7, 9
```

---

### Step 2 — Generate Odd Numbers

The loop is:

```python
for i in range(1, n + 1):
    print(i + i - 1)
```

The expression:

```text
i + i - 1
```

is the same as:

```text
2 × i - 1
```

Therefore:

```text
i = 1 → 1 + 1 - 1 = 1
i = 2 → 2 + 2 - 1 = 3
i = 3 → 3 + 3 - 1 = 5
i = 4 → 4 + 4 - 1 = 7
i = 5 → 5 + 5 - 1 = 9
```

---

# 🔍 Example

Suppose the user enters:

```text
Enter a range to generate odd numbers : 10
```

Initially:

```text
n = 10
```

Then:

```python
n = int(10 / 2)
```

So:

```text
n = 5
```

The loop becomes:

```python
range(1, 6)
```

Therefore, `i` takes the values:

```text
1, 2, 3, 4, 5
```

---

# 📊 Complete Tracing

| Step | `i` | Calculation | Output |
|---:|---:|---|---:|
| 1 | 1 | `1 + 1 - 1` | 1 |
| 2 | 2 | `2 + 2 - 1` | 3 |
| 3 | 3 | `3 + 3 - 1` | 5 |
| 4 | 4 | `4 + 4 - 1` | 7 |
| 5 | 5 | `5 + 5 - 1` | 9 |

Final output:

```text
1
3
5
7
9
```

---

# 🧮 Why Does `i + i - 1` Generate Odd Numbers?

An odd number can be represented as:

```text
2 × i - 1
```

Since:

```text
i + i = 2 × i
```

we can write:

```text
i + i - 1
```

For different values of `i`:

```text
i = 1 → 1
i = 2 → 3
i = 3 → 5
i = 4 → 7
i = 5 → 9
```

Therefore, every generated value is odd.

---

# 🔄 Pattern of Generation

```text
i        i+i-1        Odd Number

1        1+1-1        1
2        2+2-1        3
3        3+3-1        5
4        4+4-1        7
5        5+5-1        9
```

The difference between consecutive numbers is always `2`:

```text
1 → 3 → 5 → 7 → 9
    +2   +2   +2
```

---

# 🖨️ Output

For input:

```text
Enter a range to generate odd numbers : 10
```

Output:

```text
1
3
5
7
9
```

---

# 🔄 Program Flow

```text
            Input range
                 ↓
             n = n / 2
                 ↓
        Start loop from 1
                 ↓
       Calculate i+i-1
                 ↓
         Print odd number
                 ↓
        Next value of i
                 ↓
           Loop ends
```

---

# 📚 Concepts Practiced

- Python input
- `int()` conversion
- `for` loop
- `range()`
- Arithmetic expressions
- Odd number generation
- Mathematical representation of odd numbers

## 💡 Key Takeaway

The main formula used is:

```text
Odd Number = 2 × i - 1
```

In the program:

```python
i + i - 1
```

is used to generate the same result.

For example:

```text
1, 3, 5, 7, 9, ...
```

### In One Line

> **Divide the range by 2 to determine the number of odd values to generate, then use `i + i - 1` to directly generate each odd number.**