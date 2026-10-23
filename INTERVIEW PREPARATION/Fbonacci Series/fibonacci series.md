# Fibonacci Series Using Array 🔢

## 📌 Description

This Python program generates the **Fibonacci series** using a list.

In the Fibonacci series, each number is obtained by adding the **previous two numbers**.

The series starts with:

```text
0, 1
```

Then:

```text
0 + 1 = 1
1 + 1 = 2
1 + 2 = 3
2 + 3 = 5
...
```

The program stores the generated values in a list and uses:

```python
a[i] = a[i-1] + a[i-2]
```

to generate the next Fibonacci number.

---

# 💻 Program

```python
n = int(input("Enter a number to generate fibonacci series: "))

a = [0] * (n + 1)

a[0] = 0
a[1] = 1

for i in range(2, n + 1):
    a[i] = a[i-1] + a[i-2]

print(a)
```

---

# 🧠 Logic of the Program

The program works in four steps:

1. Take the number `n` from the user.
2. Create a list of size `n + 1`.
3. Store the first two Fibonacci numbers:
   ```python
   a[0] = 0
   a[1] = 1
   ```
4. Generate the remaining numbers using:
   ```python
   a[i] = a[i-1] + a[i-2]
   ```

---

# 🔑 Understanding the List Creation

The statement:

```python
a = [0] * (n + 1)
```

creates a list containing `n + 1` zeros.

For example, if:

```text
n = 7
```

then:

```text
a = [0] * 8
```

creates:

```text
[0, 0, 0, 0, 0, 0, 0, 0]
```

The list has indexes:

```text
Index:  0  1  2  3  4  5  6  7
Value:  0  0  0  0  0  0  0  0
```

Then the program sets:

```python
a[0] = 0
a[1] = 1
```

So:

```text
[0, 1, 0, 0, 0, 0, 0, 0]
```

---

# 🔍 Example

Suppose the user enters:

```text
Enter a number to generate fibonacci series: 7
```

Then:

```text
n = 7
```

The program creates:

```text
a = [0, 0, 0, 0, 0, 0, 0, 0]
```

After initializing the first two values:

```text
a = [0, 1, 0, 0, 0, 0, 0, 0]
```

Now the `for` loop starts from:

```python
i = 2
```

and continues until:

```python
i = 7
```

---

# 📊 Complete Tracing

## Initial Values

```text
n = 7

a = [0, 0, 0, 0, 0, 0, 0, 0]

a[0] = 0
a[1] = 1
```

Current array:

```text
[0, 1, 0, 0, 0, 0, 0, 0]
```

---

### Step 1 — `i = 2`

Formula:

```text
a[2] = a[1] + a[0]
```

Substitute:

```text
a[2] = 1 + 0
a[2] = 1
```

Array:

```text
[0, 1, 1, 0, 0, 0, 0, 0]
```

---

### Step 2 — `i = 3`

```text
a[3] = a[2] + a[1]
```

```text
a[3] = 1 + 1
a[3] = 2
```

Array:

```text
[0, 1, 1, 2, 0, 0, 0, 0]
```

---

### Step 3 — `i = 4`

```text
a[4] = a[3] + a[2]
```

```text
a[4] = 2 + 1
a[4] = 3
```

Array:

```text
[0, 1, 1, 2, 3, 0, 0, 0]
```

---

### Step 4 — `i = 5`

```text
a[5] = a[4] + a[3]
```

```text
a[5] = 3 + 2
a[5] = 5
```

Array:

```text
[0, 1, 1, 2, 3, 5, 0, 0]
```

---

### Step 5 — `i = 6`

```text
a[6] = a[5] + a[4]
```

```text
a[6] = 5 + 3
a[6] = 8
```

Array:

```text
[0, 1, 1, 2, 3, 5, 8, 0]
```

---

### Step 6 — `i = 7`

```text
a[7] = a[6] + a[5]
```

```text
a[7] = 8 + 5
a[7] = 13
```

Final array:

```text
[0, 1, 1, 2, 3, 5, 8, 13]
```

---

# 📋 Complete Trace Table

| `i` | `a[i-1]` | `a[i-2]` | Calculation | `a[i]` |
|---:|---:|---:|---|---:|
| 2 | 1 | 0 | `1 + 0` | 1 |
| 3 | 1 | 1 | `1 + 1` | 2 |
| 4 | 2 | 1 | `2 + 1` | 3 |
| 5 | 3 | 2 | `3 + 2` | 5 |
| 6 | 5 | 3 | `5 + 3` | 8 |
| 7 | 8 | 5 | `8 + 5` | 13 |

---

# 🔄 Fibonacci Generation

The values are generated as:

```text
a[0] = 0
a[1] = 1

a[2] = a[1] + a[0] = 1 + 0 = 1
a[3] = a[2] + a[1] = 1 + 1 = 2
a[4] = a[3] + a[2] = 2 + 1 = 3
a[5] = a[4] + a[3] = 3 + 2 = 5
a[6] = a[5] + a[4] = 5 + 3 = 8
a[7] = a[6] + a[5] = 8 + 5 = 13
```

Therefore:

```text
0, 1, 1, 2, 3, 5, 8, 13
```

---

# 🖨️ Output

For input:

```text
Enter a number to generate fibonacci series: 7
```

Output:

```text
[0, 1, 1, 2, 3, 5, 8, 13]
```

---

# 🔄 Program Flow

```text
             Input n
                ↓
       Create list of n+1
                ↓
          a[0] = 0
          a[1] = 1
                ↓
        Start loop from 2
                ↓
   a[i] = a[i-1] + a[i-2]
                ↓
        Store result in a[i]
                ↓
          Next i value
                ↓
         Repeat until n
                ↓
          Print the list
```

---

# 🧮 Main Formula

The main formula used in this program is:

```python
a[i] = a[i-1] + a[i-2]
```

This means:

> **Current Fibonacci number = Previous Fibonacci number + Number before previous**

For example:

```text
5 + 3 = 8
```

So:

```text
a[6] = 8
```

---

# 📚 Concepts Practiced

- Python lists
- List initialization
- Array indexing
- `for` loop
- Fibonacci series
- Previous-element access
- Mathematical recurrence
- Updating list elements

## 💡 Key Takeaway

The first two values are fixed:

```text
0, 1
```

Every following value is generated using:

```text
Previous value + Value before previous
```

or:

```python
a[i] = a[i-1] + a[i-2]
```

### In One Line

> **Initialize `0` and `1`, then repeatedly add the previous two elements to generate the Fibonacci series.**