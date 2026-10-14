# Length of a Number 🔢

## 📌 Description

This Python program finds the **length of a number**, which means it counts how many digits are present in the number.

The program repeatedly removes the last digit using:

```python
n = n // 10
```

For every digit removed, the `count` variable is increased by `1`.

### Example

For:

```text
12345
```

There are **5 digits**, so the length of the number is:

```text
5
```

---

# 💻 Program

```python
n = int(input("Enter a number: "))

count = 0

while(n != 0):
    r = n % 10
    n = n // 10
    count += 1

print("Length of a number is: ", count)
```

---

# 🧠 Logic of the Program

The program uses three important operations.

### 1. Extract the last digit

```python
r = n % 10
```

The `% 10` operation gives the last digit.

Example:

```text
12345 % 10 = 5
```

The variable `r` stores the extracted digit.

### 2. Remove the last digit

```python
n = n // 10
```

Integer division by `10` removes the last digit.

Example:

```text
12345 // 10 = 1234
```

### 3. Increase the count

```python
count += 1
```

Every time one digit is removed, the count increases by `1`.

The process continues until:

```text
n = 0
```

Then the loop stops.

---

# 🔍 Example

Suppose the user enters:

```text
Enter a number: 12345
```

Initial values:

```text
n = 12345
count = 0
```

The program removes one digit during every iteration.

---

# 📊 Complete Tracing

## Step 1

Current values:

```text
n = 12345
count = 0
```

Extract last digit:

```text
r = 12345 % 10
r = 5
```

Remove last digit:

```text
n = 12345 // 10
n = 1234
```

Increase count:

```text
count = 0 + 1
count = 1
```

---

## Step 2

Current values:

```text
n = 1234
count = 1
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

Increase:

```text
count = 1 + 1
count = 2
```

---

## Step 3

Current values:

```text
n = 123
count = 2
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

Increase:

```text
count = 2 + 1
count = 3
```

---

## Step 4

Current values:

```text
n = 12
count = 3
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

Increase:

```text
count = 3 + 1
count = 4
```

---

## Step 5

Current values:

```text
n = 1
count = 4
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

Increase:

```text
count = 4 + 1
count = 5
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

Final:

```text
count = 5
```

---

# 📋 Trace Table

| Step | `n` Before | `r = n % 10` | `n = n // 10` | `count` |
|---:|---:|---:|---:|---:|
| 1 | 12345 | 5 | 1234 | 1 |
| 2 | 1234 | 4 | 123 | 2 |
| 3 | 123 | 3 | 12 | 3 |
| 4 | 12 | 2 | 1 | 4 |
| 5 | 1 | 1 | 0 | 5 |

The extracted digits are:

```text
5 → 4 → 3 → 2 → 1
```

The count increases:

```text
0 → 1 → 2 → 3 → 4 → 5
```

---

# 🖨️ Output

For input:

```text
Enter a number: 12345
```

Output:

```text
Length of a number is:  5
```

---

# 🔄 Program Flow

```text
             Input Number
                  ↓
              n != 0?
             ↙       ↘
           Yes         No
            ↓           ↓
       n % 10          Stop
       Get digit
            ↓
       n = n // 10
       Remove digit
            ↓
       count += 1
            ↓
        Check again
```

---

# 🧮 Why Does This Find the Length?

Every time we perform:

```python
n = n // 10
```

**one digit is removed**.

For example:

```text
12345
 ↓
1234       → 1 digit removed
 ↓
123        → 2 digits removed
 ↓
12         → 3 digits removed
 ↓
1          → 4 digits removed
 ↓
0          → 5 digits removed
```

Therefore:

```text
Number of removals = Number of digits
```

So:

```text
count = length of the number
```

---

# 📚 Concepts Practiced

- Python input
- `while` loop
- `%` modulo operator
- `//` integer division
- Digit extraction
- Digit removal
- Counter variable
- Number manipulation

## 💡 Key Takeaway

The two main operations are:

```python
r = n % 10
```

→ extracts the last digit.

```python
n = n // 10
```

→ removes the last digit.

And:

```python
count += 1
```

→ counts how many digits were removed.

### In One Line

> **Repeatedly remove the last digit using `n // 10` and increment `count` for every removed digit until the number becomes `0`.**