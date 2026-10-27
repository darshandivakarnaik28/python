# Generate Even Numbers 🔢

## 📌 Description

This Python program generates all the **even numbers** from `2` up to the given range.

Instead of checking every number using the modulo operator `%`, the program directly generates even numbers using:

```python
i + i
```

Since:

```text
i + i = 2 × i
```

the result is always an even number.

For example, if the input is:

```text
10
```

the output is:

```text
2
4
6
8
10
```

---

# 💻 Program

```python
n = int(input("Enter the range for generate the even numbers : "))

n = int(n / 2)

for i in range(1, n + 1):
    print(i + i)
```

---

# 🧠 Logic of the Program

The program works in two main steps.

### Step 1 — Find the Number of Even Numbers

```python
n = int(n / 2)
```

If the original range is `10`:

```text
10 / 2 = 5
```

So:

```text
n = 5
```

There are 5 even numbers between 1 and 10:

```text
2, 4, 6, 8, 10
```

---

### Step 2 — Generate Even Numbers

```python
for i in range(1, n + 1):
    print(i + i)
```

The loop generates:

```text
i = 1 → 1 + 1 = 2
i = 2 → 2 + 2 = 4
i = 3 → 3 + 3 = 6
i = 4 → 4 + 4 = 8
i = 5 → 5 + 5 = 10
```

Therefore:

```text
2
4
6
8
10
```

---

# 🔍 Example

Suppose the user enters:

```text
Enter the range for generate the even numbers : 10
```

Initially:

```text
n = 10
```

Then:

```text
n = int(10 / 2)
n = 5
```

So the loop becomes:

```python
range(1, 6)
```

which generates:

```text
1, 2, 3, 4, 5
```

Each value is doubled using:

```text
i + i
```

---

# 📊 Complete Tracing

| Step | `i` | Calculation | Output |
|---:|---:|---|---:|
| 1 | 1 | `1 + 1` | 2 |
| 2 | 2 | `2 + 2` | 4 |
| 3 | 3 | `3 + 3` | 6 |
| 4 | 4 | `4 + 4` | 8 |
| 5 | 5 | `5 + 5` | 10 |

---

# 🔄 Step-by-Step Flow

For input:

```text
n = 10
```

### Before division

```text
n = 10
```

### After division

```text
n = int(10 / 2)
n = 5
```

### Loop

```text
i = 1 → 2
i = 2 → 4
i = 3 → 6
i = 4 → 8
i = 5 → 10
```

Final output:

```text
2
4
6
8
10
```

---

# 🧮 Why Does `i + i` Generate Even Numbers?

An even number is a number that can be written as:

```text
2 × i
```

Since:

```text
i + i = 2 × i
```

the result is always even.

For example:

```text
1 + 1 = 2
2 + 2 = 4
3 + 3 = 6
4 + 4 = 8
5 + 5 = 10
```

So the program does **not need to check whether a number is even**.

It directly generates even numbers.

---

# ⚠️ Important Point About the Range

This program works correctly for an even input range such as:

```text
10
```

For an odd range such as:

```text
11
```

the statement:

```python
n = int(n / 2)
```

gives:

```text
11 / 2 = 5.5
int(5.5) = 5
```

The output is still:

```text
2
4
6
8
10
```

which is correct because `10` is the largest even number ≤ `11`.

---

# 🖨️ Output

For input:

```text
Enter the range for generate the even numbers : 10
```

Output:

```text
2
4
6
8
10
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
           Calculate i + i
                  ↓
          Print even number
                  ↓
           Next value of i
                  ↓
             Loop ends
```

---

# 📚 Concepts Practiced

- Python input
- Type conversion
- `int()`
- `for` loop
- `range()`
- Arithmetic operations
- Even number generation
- Integer division/truncation
- Mathematical representation of even numbers

## 💡 Key Takeaway

The main idea of this program is:

```text
Even number = 2 × i
```

and:

```text
2 × i = i + i
```

So instead of checking:

```text
number % 2 == 0
```

the program directly generates the even numbers using:

```python
print(i + i)
```

### In One Line

> **Divide the range by 2 to find how many even numbers exist, then generate each even number using `i + i`.**