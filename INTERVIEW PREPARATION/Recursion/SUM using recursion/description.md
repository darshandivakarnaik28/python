# Sum of Numbers Using Recursion ➕

This Python program calculates the **sum of numbers from `n` to `1` using recursion**.

It uses a second parameter, `sum`, to keep track of the accumulated sum during each recursive call.

## 📌 Program

```python
def add_(n, sum):
    if n > 0:
        s = f"sum of {n}+{sum}="
        sum = sum + n
        n -= 1
        print(f"{s}{sum}")
        add_(n, sum)


add_(3, 0)
```

## 🧠 How the Program Works

The function has two parameters:

```text
n
sum
```

- `n` → The current number being added.
- `sum` → Stores the accumulated sum.

The function checks:

```python
if n > 0:
```

If the condition is true:

1. Display the current addition.
2. Add `n` to `sum`.
3. Decrease `n` by `1`.
4. Call the same function again.

The recursion stops when:

```text
n = 0
```

because:

```text
0 > 0 → False
```

---

# 🔍 Complete Program Trace

The program starts with:

```text
add_(3, 0)
```

So initially:

```text
n = 3
sum = 0
```

---

## Step 1 — `add_(3, 0)`

Check:

```text
n > 0
3 > 0 → True
```

Create:

```text
s = "sum of 3+0="
```

Calculate:

```text
sum = sum + n
sum = 0 + 3
sum = 3
```

Decrease `n`:

```text
n = n - 1
n = 3 - 1
n = 2
```

Print:

```text
sum of 3+0=3
```

Recursive call:

```text
add_(2, 3)
```

---

## Step 2 — `add_(2, 3)`

Current values:

```text
n = 2
sum = 3
```

Check:

```text
2 > 0 → True
```

Create:

```text
s = "sum of 2+3="
```

Calculate:

```text
sum = 3 + 2
sum = 5
```

Decrease `n`:

```text
n = 2 - 1
n = 1
```

Print:

```text
sum of 2+3=5
```

Recursive call:

```text
add_(1, 5)
```

---

## Step 3 — `add_(1, 5)`

Current values:

```text
n = 1
sum = 5
```

Check:

```text
1 > 0 → True
```

Create:

```text
s = "sum of 1+5="
```

Calculate:

```text
sum = 5 + 1
sum = 6
```

Decrease `n`:

```text
n = 1 - 1
n = 0
```

Print:

```text
sum of 1+5=6
```

Recursive call:

```text
add_(0, 6)
```

---

## Step 4 — `add_(0, 6)`

Current values:

```text
n = 0
sum = 6
```

Check:

```text
0 > 0 → False
```

Therefore, the `if` block is not executed.

No further recursive call is made.

**Recursion stops.**

The final sum is:

```text
6
```

---

# 📊 Complete Tracking Table

| Step | Function Call | `n` | `sum` Before | Calculation | `sum` After | Next Call |
|---|---|---:|---:|---|---:|---|
| 1 | `add_(3, 0)` | 3 | 0 | `0 + 3` | 3 | `add_(2, 3)` |
| 2 | `add_(2, 3)` | 2 | 3 | `3 + 2` | 5 | `add_(1, 5)` |
| 3 | `add_(1, 5)` | 1 | 5 | `5 + 1` | 6 | `add_(0, 6)` |
| 4 | `add_(0, 6)` | 0 | 6 | No calculation | 6 | Stop |

---

# 🖨️ Output

The program prints:

```text
sum of 3+0=3
sum of 2+3=5
sum of 1+5=6
```

So:

```text
3 + 2 + 1 = 6
```

**Final Sum = `6`**

---

# 🔄 Recursion Flow

The recursive calls happen like this:

```text
add_(3, 0)
     ↓
add_(2, 3)
     ↓
add_(1, 5)
     ↓
add_(0, 6)
     ↓
n > 0 is False
     ↓
   Stop
```

---

# 🧱 Understanding the Two Variables

### `n`

`n` tells the function which number needs to be added next.

```text
3 → 2 → 1 → 0
```

### `sum`

`sum` remembers the total calculated so far.

```text
0 → 3 → 5 → 6
```

So both values change during recursion:

```text
n:    3 → 2 → 1 → 0
sum:  0 → 3 → 5 → 6
```

---

# 🛑 Termination Condition

The recursion continues while:

```python
if n > 0:
```

When `n` becomes `0`:

```text
0 > 0 → False
```

The function stops calling itself.

This is the **termination condition** of the recursion.

---

# 📊 Simple Flow

```text
              Start
                ↓
          add_(3, 0)
                ↓
             n > 0?
            ↙      ↘
          Yes       No
           ↓         ↓
      Add n to sum  Stop
           ↓
         n -= 1
           ↓
       Print sum
           ↓
      add_(n, sum)
           ↓
      Check again
```

## 📚 Concepts Practiced

- Python functions
- Recursion
- Recursive function calls
- Function parameters
- Accumulator variable
- `if` condition
- Increment/decrement operations
- String formatting using f-strings
- Tracking a running sum
- Termination condition

## 💡 Key Idea

The important idea in this program is the **accumulator** `sum`.

```text
Start
  ↓
sum = 0
  ↓
3 + 0 = 3
  ↓
2 + 3 = 5
  ↓
1 + 5 = 6
  ↓
n = 0 → Stop
```

### In One Line

**Add the current `n` to `sum` → decrease `n` → recursively call the function → stop when `n` becomes `0`.**