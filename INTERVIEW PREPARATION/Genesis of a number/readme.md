# Genesis of a Number 🔢

## 📌 Description

This Python program demonstrates the **genesis or creation of a number**.

The program takes a number as input and reconstructs it **digit by digit using place value**.

The main idea is:

```python
space = space * 10 + r
```

Here:

- `r` represents the current digit.
- `space * 10` shifts the previously created number one place to the left.
- `+ r` places the new digit at the units position.

Before creating the number, the program first **reverses the input number** so that the digits can be processed from left to right during the creation phase.

---

# 💻 Program

```python
n = int(input("Enter a number: "))

reverse = 0

while(n != 0):
    r = n % 10
    reverse = (reverse * 10) + r
    n = n // 10

space = 0

while(reverse != 0):
    print("Socker Creation")

    r = reverse % 10

    print(space, end=" ")
    space = space * 10
    print("* 10 =", space)

    print("Placement of digit")

    print(space, end=" ")
    space = space + r
    print("+", r, "=", space)

    reverse //= 10
```

---

# 🧠 Logic of the Program

The program has **two main phases**.

### Phase 1 — Reverse the Number

The first `while` loop extracts digits from the right side using:

```python
r = n % 10
```

and builds the reversed number using:

```python
reverse = (reverse * 10) + r
```

Then the last digit is removed using:

```python
n = n // 10
```

### Phase 2 — Create the Number

The second `while` loop takes the digits from `reverse` and creates the number again.

The important operation is:

```python
space = space * 10
space = space + r
```

This can be combined as:

```python
space = space * 10 + r
```

The multiplication by `10` creates space for the next digit.

---

# 🔍 Example

Suppose the user enters:

```text
Enter a number: 12345
```

The program first reverses the number.

```text
12345 → 54321
```

Then it processes `54321` from the right side:

```text
1 → 2 → 3 → 4 → 5
```

This allows the number to be created in the original order:

```text
1 → 12 → 123 → 1234 → 12345
```

---

# 🔄 Phase 1: Reverse the Number

Initial values:

```text
n = 12345
reverse = 0
```

### Step 1

Extract last digit:

```text
r = 12345 % 10
r = 5
```

Create reverse:

```text
reverse = (0 × 10) + 5
reverse = 5
```

Remove last digit:

```text
n = 12345 // 10
n = 1234
```

---

### Step 2

```text
r = 1234 % 10
r = 4

reverse = (5 × 10) + 4
reverse = 54

n = 1234 // 10
n = 123
```

---

### Step 3

```text
r = 123 % 10
r = 3

reverse = (54 × 10) + 3
reverse = 543

n = 123 // 10
n = 12
```

---

### Step 4

```text
r = 12 % 10
r = 2

reverse = (543 × 10) + 2
reverse = 5432

n = 12 // 10
n = 1
```

---

### Step 5

```text
r = 1 % 10
r = 1

reverse = (5432 × 10) + 1
reverse = 54321

n = 1 // 10
n = 0
```

Now:

```text
n = 0
```

The first loop stops.

The reversed number is:

```text
reverse = 54321
```

---

# 📊 Phase 1 Trace Table

| Step | `n` | `r = n % 10` | `reverse` | `n = n // 10` |
|---:|---:|---:|---:|---:|
| 1 | 12345 | 5 | 5 | 1234 |
| 2 | 1234 | 4 | 54 | 123 |
| 3 | 123 | 3 | 543 | 12 |
| 4 | 12 | 2 | 5432 | 1 |
| 5 | 1 | 1 | 54321 | 0 |

---

# 🏗️ Phase 2: Genesis / Creation of the Number

Now:

```text
reverse = 54321
space = 0
```

The second loop extracts digits from `reverse`.

---

## Step 1 — Create `1`

Extract:

```text
r = 54321 % 10
r = 1
```

First:

```text
space = 0 × 10
space = 0
```

Then place the digit:

```text
space = 0 + 1
space = 1
```

So:

```text
0 × 10 = 0
0 + 1 = 1
```

Remove the digit:

```text
reverse = 54321 // 10
reverse = 5432
```

---

## Step 2 — Create `12`

Extract:

```text
r = 5432 % 10
r = 2
```

Shift the existing number:

```text
space = 1 × 10
space = 10
```

Place the new digit:

```text
space = 10 + 2
space = 12
```

So:

```text
1 × 10 = 10
10 + 2 = 12
```

---

## Step 3 — Create `123`

Extract:

```text
r = 543 % 10
r = 3
```

Shift:

```text
space = 12 × 10
space = 120
```

Place digit:

```text
space = 120 + 3
space = 123
```

---

## Step 4 — Create `1234`

Extract:

```text
r = 54 % 10
r = 4
```

Shift:

```text
space = 123 × 10
space = 1230
```

Place digit:

```text
space = 1230 + 4
space = 1234
```

---

## Step 5 — Create `12345`

Extract:

```text
r = 5 % 10
r = 5
```

Shift:

```text
space = 1234 × 10
space = 12340
```

Place digit:

```text
space = 12340 + 5
space = 12345
```

The number has now been completely created.

---

# 📊 Phase 2 Trace Table

| Step | `reverse` | `r` | `space × 10` | `space + r` | New `space` |
|---:|---:|---:|---:|---:|---:|
| 1 | 54321 | 1 | `0 × 10 = 0` | `0 + 1` | 1 |
| 2 | 5432 | 2 | `1 × 10 = 10` | `10 + 2` | 12 |
| 3 | 543 | 3 | `12 × 10 = 120` | `120 + 3` | 123 |
| 4 | 54 | 4 | `123 × 10 = 1230` | `1230 + 4` | 1234 |
| 5 | 5 | 5 | `1234 × 10 = 12340` | `12340 + 5` | 12345 |

---

# 🖨️ Output

For input:

```text
12345
```

the creation section produces:

```text
Socker Creation
0 * 10 = 0
Placement of digit
0 + 1 = 1

Socker Creation
1 * 10 = 10
Placement of digit
10 + 2 = 12

Socker Creation
12 * 10 = 120
Placement of digit
120 + 3 = 123

Socker Creation
123 * 10 = 1230
Placement of digit
1230 + 4 = 1234

Socker Creation
1234 * 10 = 12340
Placement of digit
12340 + 5 = 12345
```

---

# 🔄 Complete Program Flow

```text
             Input: 12345
                    ↓
             Extract digits
                    ↓
              Reverse number
                    ↓
                54321
                    ↓
          Extract last digit
                    ↓
          space = space × 10
                    ↓
          Add extracted digit
                    ↓
               space + r
                    ↓
              Repeat process
                    ↓
               12345
                    ↓
                  Stop
```

---

# 🧮 Main Logic of Number Creation

The most important part of the program is:

```python
space = space * 10
space = space + r
```

For example, if:

```text
space = 123
r = 4
```

First:

```text
123 × 10 = 1230
```

Multiplying by `10` shifts the digits left:

```text
123 → 1230
```

Then:

```text
1230 + 4 = 1234
```

So the new digit `4` is placed at the end.

Therefore:

```text
123 → 1234
```

---

# 📚 Concepts Practiced

- Python `while` loop
- `%` modulo operator
- `//` integer division
- Digit extraction
- Number reversal
- Place value
- Number construction
- Variable updating
- Mathematical manipulation of digits

## 💡 Key Takeaway

**Destruction** removes digits using:

```python
n = n // 10
```

**Genesis/creation** builds the number using:

```python
space = space * 10 + r
```

For example:

```text
Destruction:
12345 → 1234 → 123 → 12 → 1 → 0

Genesis:
0 → 1 → 12 → 123 → 1234 → 12345
```

### In One Line

> **Extract each digit and repeatedly multiply the existing number by 10, then add the new digit to create the number digit by digit.**