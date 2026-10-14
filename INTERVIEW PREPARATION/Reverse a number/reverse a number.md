# Reverse a Number 🔄

## 📌 Description

This Python program reverses the digits of a given number.

It uses two important operations:

```python
r = n % 10
```

to **extract the last digit**, and

```python
n = n // 10
```

to **remove the last digit**.

The extracted digit is added to the `reverse` variable using:

```python
reverse = (reverse * 10) + r
```

### Example

If the input is:

```text
12345
```

the reverse is:

```text
54321
```

---

# 💻 Program

```python
n = int(input("Enter a number: "))

num = n
reverse = 0

while(n != 0):
    r = n % 10
    n = n // 10
    reverse = (reverse * 10) + r

print("Entered Number is: ", num)
print("Reverse number is: ", reverse)
```

---

# 🧠 Logic of the Program

The program follows these steps:

1. Take a number from the user.
2. Store the original number in `num`.
3. Initialize `reverse` to `0`.
4. Extract the last digit using `% 10`.
5. Remove the last digit using `// 10`.
6. Add the extracted digit to the reverse number.
7. Repeat until `n` becomes `0`.

---

# 🔑 Important Operations

### 1. Extract the last digit

```python
r = n % 10
```

For example:

```text
12345 % 10 = 5
```

So `r` becomes `5`.

### 2. Remove the last digit

```python
n = n // 10
```

For example:

```text
12345 // 10 = 1234
```

The last digit `5` is removed.

### 3. Build the reverse

```python
reverse = (reverse * 10) + r
```

This adds the extracted digit to the end of the reverse number.

For example:

```text
reverse = 0
r = 5

reverse = (0 × 10) + 5
reverse = 5
```

Next:

```text
reverse = 5
r = 4

reverse = (5 × 10) + 4
reverse = 54
```

So the reverse is built digit by digit.

---

# 🔍 Example

Suppose the user enters:

```text
Enter a number: 12345
```

Initial values:

```text
n = 12345
num = 12345
reverse = 0
```

`num` is used to preserve the original number because `n` will change during the loop.

---

# 📊 Complete Tracing

## Step 1

Current values:

```text
n = 12345
reverse = 0
```

Extract:

```text
r = 12345 % 10
r = 5
```

Remove last digit:

```text
n = 12345 // 10
n = 1234
```

Build reverse:

```text
reverse = (0 × 10) + 5
reverse = 5
```

---

## Step 2

Current values:

```text
n = 1234
reverse = 5
```

Extract:

```text
r = 1234 % 10
r = 4
```

Remove:

```text
n = 1234 // 10
n = 123
```

Build:

```text
reverse = (5 × 10) + 4
reverse = 54
```

---

## Step 3

Current values:

```text
n = 123
reverse = 54
```

Extract:

```text
r = 123 % 10
r = 3
```

Remove:

```text
n = 123 // 10
n = 12
```

Build:

```text
reverse = (54 × 10) + 3
reverse = 543
```

---

## Step 4

Current values:

```text
n = 12
reverse = 543
```

Extract:

```text
r = 12 % 10
r = 2
```

Remove:

```text
n = 12 // 10
n = 1
```

Build:

```text
reverse = (543 × 10) + 2
reverse = 5432
```

---

## Step 5

Current values:

```text
n = 1
reverse = 5432
```

Extract:

```text
r = 1 % 10
r = 1
```

Remove:

```text
n = 1 // 10
n = 0
```

Build:

```text
reverse = (5432 × 10) + 1
reverse = 54321
```

Now:

```text
n = 0
```

Therefore:

```text
n != 0 → False
```

The loop stops.

---

# 📋 Complete Trace Table

| Step | `n` Before | `r = n % 10` | `n = n // 10` | `reverse` |
|---:|---:|---:|---:|---:|
| 1 | 12345 | 5 | 1234 | 5 |
| 2 | 1234 | 4 | 123 | 54 |
| 3 | 123 | 3 | 12 | 543 |
| 4 | 12 | 2 | 1 | 5432 |
| 5 | 1 | 1 | 0 | 54321 |

---

# 🔄 How the Reverse Is Created

The reverse number is built as:

```text
Original:
12345

Extract digits:
5 → 4 → 3 → 2 → 1

Create reverse:
0
 ↓
5
 ↓
54
 ↓
543
 ↓
5432
 ↓
54321
```

Therefore:

```text
12345 → 54321
```

---

# 🖨️ Output

```text
Enter a number: 12345
Entered Number is:  12345
Reverse number is:  54321
```

---

# 🔄 Program Flow

```text
             Input Number
                  ↓
           Store in num
                  ↓
            reverse = 0
                  ↓
              n != 0?
             ↙       ↘
           Yes         No
            ↓           ↓
        r = n % 10    Print result
            ↓
        n = n // 10
            ↓
   reverse = reverse × 10 + r
            ↓
        Check again
```

---

# 🧮 Why Do We Use `num = n`?

The statement:

```python
num = n
```

keeps a copy of the original number.

During the loop, `n` changes:

```text
12345 → 1234 → 123 → 12 → 1 → 0
```

So if we want to print the original number at the end, we need `num`.

```text
num     = 12345
n       = 0
reverse = 54321
```

Therefore:

```python
print("Entered Number is: ", num)
```

prints the original number.

---

# 📚 Concepts Practiced

- Python input
- Variables
- `while` loop
- `%` modulo operator
- `//` integer division
- Digit extraction
- Digit removal
- Number reversal
- Building a number using place value

## 💡 Key Takeaway

The three important operations are:

```python
r = n % 10
```

**Extract the last digit**

```python
n = n // 10
```

**Remove the last digit**

```python
reverse = (reverse * 10) + r
```

**Add the extracted digit to the reverse number**

### In One Line

> **Extract the last digit → remove it from the original number → add it to the reverse → repeat until the number becomes `0`.**