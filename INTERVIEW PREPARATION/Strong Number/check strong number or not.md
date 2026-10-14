# Strong Number 💪🔢

## 📌 Description

A **Strong Number** is a number in which the **sum of the factorials of all its digits is equal to the original number**.

### Example

Consider:

```text
145
```

Separate its digits:

```text
1, 4, 5
```

Find the factorial of each digit:

```text
1! = 1
4! = 24
5! = 120
```

Add them:

```text
1! + 4! + 5!
= 1 + 24 + 120
= 145
```

Since:

```text
145 = 145
```

`145` is a **Strong Number**.

---

# 💻 Program

```python
n = int(input("Enter a number:"))

sum = 0
copy = n

print("sum of ", end="")

while(n != 0):
    r = n % 10
    n = n // 10

    fact = 1

    for i in range(1, r + 1):
        fact *= i

    sum += fact

    print(f"{i}! ", end="")

print("is =", sum)

if(sum == copy):
    print(copy, "is Strong Number")
else:
    print(copy, "is Not a Strong Number")
```

---

# 🧠 Logic of the Program

The program works in **four main steps**:

1. Extract each digit from the number.
2. Find the factorial of each digit.
3. Add all the factorials.
4. Compare the sum with the original number.

The important operations are:

### Extract the digit

```python
r = n % 10
```

This gives the last digit.

Example:

```text
145 % 10 = 5
```

### Remove the digit

```python
n = n // 10
```

This removes the last digit.

```text
145 // 10 = 14
```

### Find factorial

```python
fact = 1

for i in range(1, r + 1):
    fact *= i
```

For example, if:

```text
r = 5
```

then:

```text
5! = 1 × 2 × 3 × 4 × 5
   = 120
```

### Add factorial to the sum

```python
sum += fact
```

Each digit's factorial is added to `sum`.

---

# 🔍 Example

Let's take:

```text
Enter a number: 145
```

Initial values:

```text
n = 145
copy = 145
sum = 0
```

`copy` stores the original number because `n` will change during the loop.

---

# 📊 Complete Tracing

## Step 1 — Extract `5`

Current value:

```text
n = 145
sum = 0
```

Extract last digit:

```text
r = 145 % 10
r = 5
```

Remove last digit:

```text
n = 145 // 10
n = 14
```

Now find `5!`:

```text
fact = 1

1 × 2 × 3 × 4 × 5
= 120
```

So:

```text
sum = 0 + 120
sum = 120
```

---

## Step 2 — Extract `4`

Current value:

```text
n = 14
sum = 120
```

Extract:

```text
r = 14 % 10
r = 4
```

Remove:

```text
n = 14 // 10
n = 1
```

Find factorial:

```text
4! = 1 × 2 × 3 × 4
   = 24
```

Add:

```text
sum = 120 + 24
sum = 144
```

---

## Step 3 — Extract `1`

Current value:

```text
n = 1
sum = 144
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

Find factorial:

```text
1! = 1
```

Add:

```text
sum = 144 + 1
sum = 145
```

Now:

```text
n = 0
```

Therefore:

```text
n != 0 → False
```

The `while` loop stops.

---

# 📋 Trace Table

| Step | `n` Before | Digit `r` | Factorial | `sum` |
|---:|---:|---:|---:|---:|
| 1 | 145 | 5 | `5! = 120` | 120 |
| 2 | 14 | 4 | `4! = 24` | 144 |
| 3 | 1 | 1 | `1! = 1` | 145 |

Final values:

```text
copy = 145
sum = 145
```

Comparison:

```text
sum == copy
145 == 145
True
```

Therefore, `145` is a Strong Number.

---

# 🔄 Program Flow

```text
              Input Number
                   ↓
             Store in copy
                   ↓
              sum = 0
                   ↓
               n != 0?
              ↙       ↘
            Yes         No
             ↓           ↓
       Extract digit     Compare
          n % 10       sum and copy
             ↓           ↓
        Remove digit    Equal?
          n // 10      ↙     ↘
             ↓        Yes     No
       Find factorial   ↓       ↓
             ↓       Strong   Not Strong
        Add to sum
             ↓
         Repeat loop
```

---

# 🧮 How Factorial Is Calculated

The factorial of a number `n` is the multiplication of all positive integers from `1` to `n`.

For example:

```text
3! = 1 × 2 × 3 = 6

4! = 1 × 2 × 3 × 4 = 24

5! = 1 × 2 × 3 × 4 × 5 = 120
```

In the program:

```python
fact = 1

for i in range(1, r + 1):
    fact *= i
```

The loop calculates the factorial of the extracted digit `r`.

---

# 🖨️ Output

For input:

```text
Enter a number: 145
```

Output:

```text
sum of 5! 4! 1! is = 145
145 is Strong Number
```

*The factorials are printed in reverse digit order because the program extracts digits from right to left.*

---

# 🔄 Complete Example

```text
Original Number = 145

             ↓ Extract 5

5! = 120
sum = 120

             ↓ Extract 4

4! = 24
sum = 144

             ↓ Extract 1

1! = 1
sum = 145

             ↓

sum = 145
copy = 145

             ↓

145 == 145

             ↓

Strong Number
```

---

# 📚 Concepts Practiced

- Python input
- Variables
- `while` loop
- `for` loop
- `%` modulo operator
- `//` integer division
- Digit extraction
- Factorial calculation
- Accumulator variable
- Conditional statements
- Number manipulation

## 💡 Key Takeaway

The main logic is:

```text
Extract digit
     ↓
Find its factorial
     ↓
Add factorial to sum
     ↓
Repeat for all digits
     ↓
Compare sum with original number
```

A number is a **Strong Number** if:

```text
Sum of factorials of digits = Original number
```

### In One Line

> **Extract each digit → calculate its factorial → add all factorials → compare the result with the original number.**