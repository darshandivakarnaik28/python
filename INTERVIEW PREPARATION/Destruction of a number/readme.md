# Destruction of a Number 🔢

## 📌 Description

This Python program demonstrates the **destruction of a number**.

Destruction of a number means **removing the last digit of a number repeatedly until no digits are left**.

This is done using:

```python
n = n // 10
```

The `//` operator performs **integer division**, so dividing a number by `10` removes its last digit.

### Example

If:

```text
n = 12345
```

then:

```text
12345 // 10 = 1234
1234  // 10 = 123
123   // 10 = 12
12    // 10 = 1
1     // 10 = 0
```

So the number is destroyed digit by digit from the **right side**.

---

# 💻 Program

```python
n = int(input("Enter a number: "))

while(n != 0):
    print(n, "// 10 = ", end="")
    n = n // 10
    print(n)
```

---

# 🧠 Logic of the Program

The program uses a `while` loop:

```python
while(n != 0):
```

The loop continues as long as `n` is not `0`.

Inside the loop:

```python
n = n // 10
```

removes the last digit of `n`.

For example:

```text
12345 // 10 = 1234
```

The last digit `5` is removed.

The process continues until:

```text
n = 0
```

At that point:

```text
n != 0
```

becomes false, so the loop stops.

---

# 🔍 Example

Suppose the user enters:

```text
Enter a number: 12345
```

Initial value:

```text
n = 12345
```

---

# 📊 Complete Tracing

### Step 1

Current value:

```text
n = 12345
```

Condition:

```text
12345 != 0 → True
```

Perform:

```text
n = n // 10
n = 12345 // 10
n = 1234
```

Output:

```text
12345 // 10 = 1234
```

---

### Step 2

Current value:

```text
n = 1234
```

Condition:

```text
1234 != 0 → True
```

Perform:

```text
n = 1234 // 10
n = 123
```

Output:

```text
1234 // 10 = 123
```

---

### Step 3

Current value:

```text
n = 123
```

Perform:

```text
n = 123 // 10
n = 12
```

Output:

```text
123 // 10 = 12
```

---

### Step 4

Current value:

```text
n = 12
```

Perform:

```text
n = 12 // 10
n = 1
```

Output:

```text
12 // 10 = 1
```

---

### Step 5

Current value:

```text
n = 1
```

Perform:

```text
n = 1 // 10
n = 0
```

Output:

```text
1 // 10 = 0
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

# 📋 Trace Table

| Step | `n` Before | Operation | `n` After |
|---:|---:|---|---:|
| 1 | 12345 | `12345 // 10` | 1234 |
| 2 | 1234 | `1234 // 10` | 123 |
| 3 | 123 | `123 // 10` | 12 |
| 4 | 12 | `12 // 10` | 1 |
| 5 | 1 | `1 // 10` | 0 |

---

# 🖨️ Output

```text
Enter a number: 12345

12345 // 10 = 1234
1234 // 10 = 123
123 // 10 = 12
12 // 10 = 1
1 // 10 = 0
```

---

# 🔄 Destruction Flow

```text
        12345
          ↓
       // 10
          ↓
        1234
          ↓
       // 10
          ↓
         123
          ↓
       // 10
          ↓
          12
          ↓
       // 10
          ↓
           1
          ↓
       // 10
          ↓
           0
          ↓
         STOP
```

---

# 🧮 Why Does `// 10` Remove the Last Digit?

The `//` operator performs **floor division**.

For positive integers:

```text
12345 // 10 = 1234
```

Normal division gives:

```text
12345 / 10 = 1234.5
```

But integer division keeps only the integer part:

```text
12345 // 10 = 1234
```

Therefore, the last digit `5` is removed.

Another example:

```text
786 // 10 = 78
78  // 10 = 7
7   // 10 = 0
```

---

# 📚 Concepts Practiced

- Python input
- Integer conversion using `int()`
- `while` loop
- Integer/floor division `//`
- Updating a variable
- Number digit manipulation
- Loop termination condition

## 💡 Key Takeaway

The main operation in this program is:

```python
n = n // 10
```

It removes **one digit from the right side** of the number during every iteration.

**In one line:**

> **Repeatedly divide the number by 10 using `//` until the number becomes 0.**