# Generate Natural Numbers 🔢

## 📌 Description

This Python program prints the **natural numbers** from `1` to the given range.

Natural numbers start from:

```text
1, 2, 3, 4, 5, ...
```

The user enters the ending value `n`, and the program uses a `for` loop to print every number from `1` to `n`.

For example, if the user enters:

```text
5
```

the output will be:

```text
1
2
3
4
5
```

---

# 💻 Program

```python
n = int(input("Enter the range to generate natural numbers : "))

for i in range(1, n + 1):
    print(i)
```

---

# 🧠 Logic of the Program

The program has two main steps:

### 1. Take the Range

```python
n = int(input("Enter the range to generate natural numbers : "))
```

The user enters the maximum natural number.

For example:

```text
n = 5
```

---

### 2. Generate Natural Numbers

```python
for i in range(1, n + 1):
    print(i)
```

The `range()` function starts from `1` and stops before `n + 1`.

Therefore:

```text
range(1, 6)
```

generates:

```text
1, 2, 3, 4, 5
```

Each value of `i` is printed.

---

# 🔍 Example

Suppose the user enters:

```text
Enter the range to generate natural numbers : 5
```

Then:

```text
n = 5
```

The loop becomes:

```python
range(1, 6)
```

The values generated are:

```text
1
2
3
4
5
```

---

# 📊 Complete Tracing

| Step | `i` | Output |
|---:|---:|---:|
| 1 | 1 | 1 |
| 2 | 2 | 2 |
| 3 | 3 | 3 |
| 4 | 4 | 4 |
| 5 | 5 | 5 |

After `i = 5`, the loop ends because there are no more values in:

```python
range(1, 6)
```

---

# 🧮 Understanding `range(1, n+1)`

The statement:

```python
range(1, n + 1)
```

has:

- Starting value = `1`
- Ending value = `n + 1`
- The ending value is **not included**

For example, if:

```text
n = 5
```

then:

```python
range(1, 6)
```

produces:

```text
1, 2, 3, 4, 5
```

The `+1` is used because Python's `range()` excludes the ending value.

---

# 🖨️ Output

For input:

```text
Enter the range to generate natural numbers : 5
```

Output:

```text
1
2
3
4
5
```

---

# 🔄 Program Flow

```text
            Input n
               ↓
       Start i from 1
               ↓
         Is i ≤ n?
          ↙     ↘
        Yes      No
         ↓        ↓
      Print i    Stop
         ↓
       i = i + 1
         ↓
       Repeat
```

---

# 📚 Concepts Practiced

- Python input
- Integer conversion using `int()`
- `for` loop
- `range()`
- Natural numbers
- Sequential number generation

## 💡 Key Takeaway

The main logic is:

```python
for i in range(1, n + 1):
    print(i)
```

This generates every natural number from `1` to `n`.

### In One Line

> **Take `n` as the ending range and use a `for` loop from `1` to `n` to print the natural numbers.**