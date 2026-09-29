# Sum Using Double Recursion 🔁➕

This Python program demonstrates **double recursion (binary recursion)** while performing addition.

Each recursive function call creates **two more recursive calls**.

The program also uses an `add` variable to keep track of the accumulated sum.

## 📌 Program

```python
def add_(n, add):
    if n > 0:
        s = f"sum of {n}+{add}="
        add += n
        n -= 1
        print(f"{s}{add}")
        add_(n, add)
        add_(n, add)


add_(3, 0)
```

## 🧠 How the Program Works

The function has two parameters:

```text
n
add
```

- `n` → The current number being added.
- `add` → Stores the accumulated sum.

The function first checks:

```python
if n > 0:
```

If true:

1. Create the string showing the current addition.
2. Add `n` to `add`.
3. Decrease `n` by `1`.
4. Print the current calculation.
5. Call `add_(n, add)` **first time**.
6. Call `add_(n, add)` **second time**.

The important part is:

```python
add_(n, add)
add_(n, add)
```

Therefore, this is **double recursion**.

---

# 🔍 Complete Program Trace

The program starts with:

```text
add_(3, 0)
```

So:

```text
n = 3
add = 0
```

---

## Step 1 — `add_(3, 0)`

Condition:

```text
3 > 0 → True
```

Create:

```text
s = "sum of 3+0="
```

Add:

```text
add = 0 + 3
add = 3
```

Decrease:

```text
n = 3 - 1
n = 2
```

Print:

```text
sum of 3+0=3
```

Now two recursive calls are made:

```text
add_(2, 3)   ← First
add_(2, 3)   ← Second
```

The first call must completely finish before the second call starts.

---

# 🌳 Recursion Tree

The complete recursion structure can be represented as:

```text
                         add_(3,0)
                       /           \
                      /             \
                 add_(2,3)       add_(2,3)
                  /     \           /     \
                 /       \         /       \
            add_(1,5)  add_(1,5) add_(1,5) add_(1,5)
             / \        / \       / \        / \
            ↓   ↓      ↓   ↓     ↓   ↓      ↓   ↓
         add(0,6) ... add(0,6)  add(0,6) ... add(0,6)
```

Every call where `n > 0` creates **two more calls**.

---

# 📊 First Branch Complete Trace

After the first call:

```text
add_(2, 3)
```

### `add_(2, 3)`

```text
n = 2
add = 3
```

Calculate:

```text
add = 3 + 2
add = 5

n = 2 - 1
n = 1
```

Prints:

```text
sum of 2+3=5
```

Then:

```text
add_(1, 5)
add_(1, 5)
```

---

## First `add_(1, 5)`

Calculate:

```text
add = 5 + 1
add = 6

n = 1 - 1
n = 0
```

Print:

```text
sum of 1+5=6
```

Then:

```text
add_(0, 6)
add_(0, 6)
```

For both calls:

```text
0 > 0 → False
```

So they stop.

---

## Second `add_(1, 5)`

The second `add_(1, 5)` then executes.

It also prints:

```text
sum of 1+5=6
```

Then makes:

```text
add_(0, 6)
add_(0, 6)
```

Both stop.

Therefore, the **first `add_(2,3)` branch is now completely finished**.

---

# 📊 Second Branch

Now the second `add_(2,3)` from the original `add_(3,0)` starts.

It follows exactly the same process:

```text
add_(2,3)
    ↓
add_(1,5)
    ↓
add_(0,6)
```

and another:

```text
add_(1,5)
    ↓
add_(0,6)
```

---

# 🖨️ Complete Output

The program prints:

```text
sum of 3+0=3
sum of 2+3=5
sum of 1+5=6
sum of 1+5=6
sum of 2+3=5
sum of 1+5=6
sum of 1+5=6
```

So:

```text
3  → printed 1 time
5  → printed 2 times
6  → printed 4 times
```

Total number of print operations:

```text
1 + 2 + 4 = 7
```

---

# 📊 Complete Tracking Table

| Call | `n` | `add` Before | Calculation | `add` After | Prints |
|---|---:|---:|---|---:|---|
| `add_(3,0)` | 3 | 0 | `0 + 3` | 3 | `sum of 3+0=3` |
| First `add_(2,3)` | 2 | 3 | `3 + 2` | 5 | `sum of 2+3=5` |
| First `add_(1,5)` | 1 | 5 | `5 + 1` | 6 | `sum of 1+5=6` |
| `add_(0,6)` | 0 | 6 | No calculation | 6 | Nothing |
| `add_(0,6)` | 0 | 6 | No calculation | 6 | Nothing |
| Second `add_(1,5)` | 1 | 5 | `5 + 1` | 6 | `sum of 1+5=6` |
| `add_(0,6)` | 0 | 6 | No calculation | 6 | Nothing |
| `add_(0,6)` | 0 | 6 | No calculation | 6 | Nothing |
| Second `add_(2,3)` | 2 | 3 | `3 + 2` | 5 | `sum of 2+3=5` |
| First `add_(1,5)` | 1 | 5 | `5 + 1` | 6 | `sum of 1+5=6` |
| `add_(0,6)` | 0 | 6 | No calculation | 6 | Nothing |
| `add_(0,6)` | 0 | 6 | No calculation | 6 | Nothing |
| Second `add_(1,5)` | 1 | 5 | `5 + 1` | 6 | `sum of 1+5=6` |
| `add_(0,6)` | 0 | 6 | No calculation | 6 | Nothing |
| `add_(0,6)` | 0 | 6 | No calculation | 6 | Nothing |

---

# 🔄 Execution Flow

The actual execution order is:

```text
add_(3,0)
    ↓
add_(2,3)        ← First
    ↓
add_(1,5)        ← First
    ↓
add_(0,6)
    ↓
add_(0,6)
    ↓
add_(1,5)        ← Second
    ↓
add_(0,6)
    ↓
add_(0,6)
    ↓
add_(2,3)        ← Second
    ↓
add_(1,5)
    ↓
add_(0,6)
    ↓
add_(0,6)
    ↓
add_(1,5)
    ↓
add_(0,6)
    ↓
add_(0,6)
```

---

# 🧱 Why Is This Double Recursion?

Normal recursion:

```text
Function
   ↓
Function
   ↓
Function
```

Double recursion:

```text
             Function
             /      \
            ↓        ↓
        Function   Function
         /   \      /   \
        ↓     ↓    ↓     ↓
```

Your program contains:

```python
add_(n, add)
add_(n, add)
```

Therefore, **each active call creates two recursive calls**.

---

# 🛑 Termination Condition

The recursion stops when:

```python
if n > 0:
```

becomes false.

When:

```text
n = 0
```

we get:

```text
0 > 0 → False
```

No more recursive calls are made.

This is the termination condition.

---

# 📊 Simple Flow

```text
                  add_(3,0)
                 /         \
                ↓           ↓
           add_(2,3)    add_(2,3)
            /    \        /    \
           ↓      ↓      ↓      ↓
       add_(1,5) add_(1,5) add_(1,5) add_(1,5)
          / \       / \      / \       / \
         ↓   ↓     ↓   ↓    ↓   ↓     ↓   ↓
       n=0 n=0   n=0 n=0  n=0 n=0   n=0 n=0
```

## 📚 Concepts Practiced

- Python functions
- Recursion
- Double/binary recursion
- Recursive call tree
- Accumulator variable
- Function parameters
- `if` condition
- Increment/decrement
- f-strings
- Call stack
- Termination condition

## 💡 Key Idea

This program combines **two concepts**:

### 1. Accumulator

The `add` variable carries the accumulated value:

```text
0 → 3 → 5 → 6
```

### 2. Double Recursion

Each call creates two more calls:

```text
add_(n, add)
add_(n, add)
```

Therefore, this is a **double recursion example with an accumulator**.

### In One Line

**Add `n` to the accumulated value → decrease `n` → make two recursive calls → repeat until `n` becomes `0`.**