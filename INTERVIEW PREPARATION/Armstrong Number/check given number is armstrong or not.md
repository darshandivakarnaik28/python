# Armstrong Number 🔢

## 📌 Description

An **Armstrong Number** is a number in which the **sum of each digit raised to the power of the total number of digits is equal to the original number**.

### Example

Consider the number:

```text id="c5q8w0"
153
```

It has **3 digits**.

Therefore:

```text id="h6a5k2"
1³ + 5³ + 3³
```

Calculate:

```text id="z8a3xk"
1³ = 1
5³ = 125
3³ = 27
```

Sum:

```text id="y5r8cb"
1 + 125 + 27 = 153
```

Since:

```text id="lq5e7w"
153 = 153
```

`153` is an **Armstrong Number**.

---

# 💻 Program

```python
n = int(input("Enter a number: "))

copy = n
count = 0

# Find the number of digits
while(n != 0):
    r = n % 10
    n = n // 10
    count += 1

# Restore original number
n = copy

print("Sum of", end=" ")

sum = 0

# Calculate Armstrong sum
while(n != 0):
    r = n % 10
    sum = sum + r ** count
    print(f"{r}**{count}", end=" ")
    n = n // 10

print("=", sum)

if(sum == copy):
    print(copy, "is a Armstrong Number")
else:
    print(copy, "is Not an Armstrong Number")
```

---

# 🧠 Logic of the Program

The program works in **three main phases**:

### Phase 1 — Count the Digits

The first `while` loop finds how many digits are present.

```python
while(n != 0):
    r = n % 10
    n = n // 10
    count += 1
```

For `153`:

```text
153 → 15 → 1 → 0
```

Therefore:

```text
count = 3
```

---

### Phase 2 — Calculate the Armstrong Sum

The original number is restored:

```python
n = copy
```

Then every digit is extracted and raised to the power `count`.

```python
sum = sum + r ** count
```

For `153`:

```text
1³ + 5³ + 3³
```

---

### Phase 3 — Compare the Result

Finally:

```python
if(sum == copy):
```

If the calculated sum is equal to the original number, it is an Armstrong Number.

Otherwise, it is not.

---

# 🔑 Important Operations

## 1. Extract the Last Digit

```python
r = n % 10
```

Example:

```text
153 % 10 = 3
```

So:

```text
r = 3
```

---

## 2. Remove the Last Digit

```python
n = n // 10
```

Example:

```text
153 // 10 = 15
```

The last digit is removed.

---

## 3. Count the Digits

```python
count += 1
```

Every time one digit is removed, `count` increases.

For `153`:

```text
0 → 1 → 2 → 3
```

So:

```text
count = 3
```

---

## 4. Calculate the Power

```python
r ** count
```

The `**` operator is the **exponentiation operator**.

For example:

```text
5 ** 3 = 125
```

---

# 🔍 Example

Suppose the user enters:

```text
Enter a number: 153
```

Initial values:

```text
n = 153
copy = 153
count = 0
```

---

# 📊 Phase 1 — Finding Number of Digits

### Step 1

```text
n = 153
r = 153 % 10 = 3
n = 153 // 10 = 15
count = 1
```

### Step 2

```text
n = 15
r = 15 % 10 = 5
n = 15 // 10 = 1
count = 2
```

### Step 3

```text
n = 1
r = 1 % 10 = 1
n = 1 // 10 = 0
count = 3
```

Now:

```text
n = 0
```

The loop stops.

Therefore:

```text
count = 3
```

---

# 📋 Digit Counting Trace

| Step | `n` Before | `r = n % 10` | `n = n // 10` | `count` |
|---:|---:|---:|---:|---:|
| 1 | 153 | 3 | 15 | 1 |
| 2 | 15 | 5 | 1 | 2 |
| 3 | 1 | 1 | 0 | 3 |

---

# 🔄 Phase 2 — Armstrong Calculation

The original number is restored:

```text
n = copy
n = 153
```

And:

```text
count = 3
sum = 0
```

Now calculate each digit's power.

---

## Step 1 — Digit `3`

```text
r = 153 % 10
r = 3
```

Calculate:

```text
3³ = 27
```

Update sum:

```text
sum = 0 + 27
sum = 27
```

Remove digit:

```text
n = 153 // 10
n = 15
```

---

## Step 2 — Digit `5`

```text
r = 15 % 10
r = 5
```

Calculate:

```text
5³ = 125
```

Update:

```text
sum = 27 + 125
sum = 152
```

Remove digit:

```text
n = 15 // 10
n = 1
```

---

## Step 3 — Digit `1`

```text
r = 1 % 10
r = 1
```

Calculate:

```text
1³ = 1
```

Update:

```text
sum = 152 + 1
sum = 153
```

Remove:

```text
n = 1 // 10
n = 0
```

The loop stops.

---

# 📋 Armstrong Calculation Trace

| Step | `n` Before | Digit `r` | Calculation | `sum` |
|---:|---:|---:|---|---:|
| 1 | 153 | 3 | `3³ = 27` | 27 |
| 2 | 15 | 5 | `5³ = 125` | 152 |
| 3 | 1 | 1 | `1³ = 1` | 153 |

Final values:

```text
copy = 153
sum = 153
```

Comparison:

```text
sum == copy

153 == 153

True
```

Therefore:

```text
153 is a Armstrong Number
```

---

# 🖨️ Output

```text
Enter a number: 153

Sum of 3**3 5**3 1**3 = 153
153 is a Armstrong Number
```

*The digits are displayed from right to left because the program extracts the last digit first.*

---

# 🔄 Complete Program Flow

```text
              Input Number
                   ↓
             Store in copy
                   ↓
             Count digits
                   ↓
               count = 3
                   ↓
            Restore n = copy
                   ↓
             Extract digit
                   ↓
          Calculate r ** count
                   ↓
              Add to sum
                   ↓
             Extract next digit
                   ↓
                Repeat
                   ↓
             Compare sum
             with original
              ↙       ↘
           Equal     Not Equal
             ↓           ↓
       Armstrong    Not Armstrong
```

---

# 🧮 Armstrong Formula

If a number contains `n` digits:

```text
Number = d₁d₂d₃...dₙ
```

Then it is an Armstrong Number if:

```text
d₁ⁿ + d₂ⁿ + d₃ⁿ + ... + dₙⁿ = Number
```

For `153`:

```text
1³ + 5³ + 3³ = 153
```

For `9474`:

```text
9⁴ + 4⁴ + 7⁴ + 4⁴ = 9474
```

---

# 📚 Concepts Practiced

- Python input
- `while` loop
- `%` modulo operator
- `//` integer division
- Digit extraction
- Counting digits
- Exponentiation operator `**`
- Accumulator variable
- Conditional statements
- Number manipulation

## 💡 Key Takeaway

The program uses:

```python
r = n % 10
```

to **extract each digit**.

```python
n = n // 10
```

to **remove each digit**.

```python
r ** count
```

to **raise each digit to the power of the number of digits**.

Finally:

```python
if(sum == copy):
```

checks whether the calculated Armstrong sum equals the original number.

### In One Line

> **Count the digits → extract each digit → raise it to the digit count → add the results → compare the sum with the original number.**