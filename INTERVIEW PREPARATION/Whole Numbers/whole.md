# Generate Whole Numbers 🔢

## 📌 Description

This Python program generates and prints **whole numbers** starting from `0` up to the given range.

Whole numbers are:

```text
0, 1, 2, 3, 4, 5, ...
```

The program uses:

```python
i - 1
```

to generate the numbers starting from `0`.

For example, if the user enters:

```text
5
```

the output will be:

```text
0
1
2
3
4
5
```

---

# 💻 Program

```python
n = int(input("Enter the range to generate the whole numbers : "))

for i in range(1, n + 2):
    print(i - 1)
```

---

# 🧠 Logic of the Program

The program uses a `for` loop to generate values of `i`.

```python
for i in range(1, n + 2):
```

The loop starts from:

```text
i = 1
```

and continues up to:

```text
i = n + 1
```

The program prints:

```python
i - 1
```

Therefore, when `i` starts at `1`:

```text
1 - 1 = 0
```

This allows the program to start printing from `0`.

---

# 🔍 Example

Suppose the user enters:

```text
Enter the range to generate the whole numbers : 5
```

Then:

```text
n = 5
```

The loop becomes:

```python
range(1, 7)
```

Since the ending value of `range()` is excluded, the values of `i` are:

```text
1, 2, 3, 4, 5, 6
```

Now the program prints `i - 1`.

---

# 📊 Complete Tracing

| Step | `i` | Calculation `i-1` | Output |
|---:|---:|---:|---:|
| 1 | 1 | `1 - 1` | 0 |
| 2 | 2 | `2 - 1` | 1 |
| 3 | 3 | `3 - 1` | 2 |
| 4 | 4 | `4 - 1` | 3 |
| 5 | 5 | `5 - 1` | 4 |
| 6 | 6 | `6 - 1` | 5 |

Final output:

```text
0
1
2
3
4
5
```

---

# 🧮 Why `range(1, n+2)`?

Normally, to generate `1` to `n`, we use:

```python
range(1, n + 1)
```

But here we want to print:

```text
0 to n
```

Since the program prints:

```python
i - 1
```

we need one additional iteration.

Therefore:

```python
range(1, n + 2)
```

For `n = 5`:

```text
range(1, 7)
```

produces:

```text
1, 2, 3, 4, 5, 6
```

After subtracting `1`:

```text
0, 1, 2, 3, 4, 5
```

---

# 🔄 Program Flow

```text
             Input n
                ↓
        Start i from 1
                ↓
        Is i ≤ n+1 ?
          ↙       ↘
        Yes        No
         ↓          ↓
      Print i-1    Stop
         ↓
      Increase i
         ↓
       Repeat
```

---

# 🖨️ Output

For input:

```text
Enter the range to generate the whole numbers : 5
```

Output:

```text
0
1
2
3
4
5
```

---

# 📚 Concepts Practiced

- Python input
- `int()` conversion
- `for` loop
- `range()`
- Arithmetic expression
- Whole number generation
- Loop tracing

## 💡 Key Takeaway

The main idea is:

```python
print(i - 1)
```

Since `i` starts from `1`, subtracting `1` makes the first output `0`.

```text
i:       1  2  3  4  5  6
          ↓  ↓  ↓  ↓  ↓  ↓
i - 1:   0  1  2  3  4  5
```

### In One Line

> **Start the loop from `1` and print `i-1` to generate whole numbers from `0` to `n`.**